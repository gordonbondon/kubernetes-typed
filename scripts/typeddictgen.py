#!/usr/bin/env python3

"""Generating kubernetes model dicts."""

import inspect
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, cast

from jinja2 import Environment, FileSystemLoader
from kubernetes import client as kubernetes_client

from kubernetes_typed.plugin import (
    ATTRIBUTE_NAME_ATTRIBUTE,
    KUBERNETES_CLIENT_PREFIX,
    NATIVE_TYPES_MAPPING,
    OPENAPI_ATTRIBUTE,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from scripts.generate_utils import PROJECT_DIRECTORY, comment_codegen, format_codegen

DICT_CLIENT_TEMPLATE_DIRECTORY = PROJECT_DIRECTORY / "scripts" / "templates" / "typeddict"
DICT_CLIENT_DIRECTORY = PROJECT_DIRECTORY / "kubernetes_typed" / "client"
DICT_CLIENT_MODELS_DIRECTORY = DICT_CLIENT_DIRECTORY / "models"


class Attribute:
    """Represents parsed state of kubernetes client model attribute."""

    def __init__(self, name: str, class_name: str, model_name: str) -> None:
        """Parse attribute parameters."""
        self.name = name
        self.class_name = class_name
        self.model_name = model_name
        self.direct_import: List[str] = []
        self.typing_import: List[str] = []
        self.model_import: Dict[str, List[str]] = {}

        self.type = self.parse_type(class_name)

    def parse_type(self, class_name: str) -> str:
        """Get attribute type from its class name."""
        # Reference kubernetes.client.api_client.deserialize
        if class_name.startswith("list["):
            self.typing_import.append("List")

            sub_class_name = re.match(r"list\[(.*)\]", class_name).group(1)  # type: ignore

            typ: str = self.parse_type(sub_class_name)

            return "List[{0}]".format(typ)

        if class_name.startswith("dict("):
            self.typing_import.append("Dict")

            key_name = re.match(r"dict\(([^,]*), (.*)\)", class_name).group(1)  # type: ignore
            sub_class_name = re.match(r"dict\(([^,]*), (.*)\)", class_name).group(2)  # type: ignore

            key = self.parse_type(key_name)
            typ = self.parse_type(sub_class_name)

            return "Dict[{0}, {1}]".format(key, typ)

        if NATIVE_TYPES_MAPPING.get(class_name) is not None:
            klass = NATIVE_TYPES_MAPPING[class_name]
            module = klass.__module__

            if module == "builtins":
                return "{0}".format(klass.__qualname__)

            self.direct_import.append(module)
            return "{0}.{1}".format(module, klass.__qualname__)

        klass = getattr(kubernetes_client, class_name, None)

        if klass is None:
            raise NameError("Attribute with missing model: {0}".format(class_name))

        module = klass.__module__.replace("kubernetes.", "kubernetes_typed.")
        typ = "{0}Dict".format(klass.__qualname__)

        # recursive types not supported https://github.com/python/mypy/issues/731
        if typ == self.model_name:
            self.typing_import.append("Any")
            self.typing_import.append("Dict")
            typ = "Dict[Any, Any]"
        else:
            if self.model_import.get(module) is not None:
                self.model_import[module].append(typ)
            else:
                self.model_import[module] = []
                self.model_import[module].append(typ)

        return typ


class Model:
    """Represents parsed state of kubernetes client model."""

    def __init__(self, class_name: str, klass: object) -> None:
        """Parse model parameters."""
        self.class_name = class_name
        self.klass = klass

        if not filter_models_classes(klass):
            raise NameError("Incompatible module for Models class: {0}".format(klass.__module__))

        self.module_full_name = klass.__module__.replace("kubernetes.", "kubernetes_typed.")
        self.module_name = klass.__module__.rpartition(".")[2]
        self.name = "{0}Dict".format(class_name)

        oapi = getattr(klass, OPENAPI_ATTRIBUTE)
        attrs = getattr(klass, ATTRIBUTE_NAME_ATTRIBUTE)

        self.attributes: List[Attribute] = []

        for name, typ in oapi.items():
            self.attributes.append(Attribute(attrs[name], typ, self.name))

        self.direct_import = self.uniq_imports_list("direct_import")
        self.typing_import = self.uniq_imports_list("typing_import")
        self.model_import = self.uniq_imports_dict("model_import")

    def uniq_imports_dict(self, import_type: str) -> Dict[str, List[str]]:
        """Get uniq client import for the model."""
        model_import: Dict[str, List[str]] = {}

        # get all imports
        imports = [getattr(attr, import_type, None) for attr in self.attributes]

        for combo in cast(List[Dict[str, List[str]]], imports):
            for module, imp in combo.items():
                if model_import.get(module) is not None:
                    model_import[module].extend(imp)
                else:
                    model_import[module] = []
                    model_import[module].extend(imp)

        # uniq and sort
        for module, models in model_import.items():
            mod = models
            mod = list(set(mod))
            mod.sort()
            model_import[module] = mod

        return model_import

    def uniq_imports_list(self, import_type: str) -> List[str]:
        """Get uniq import for the model."""
        # get all imports
        imports = [getattr(attr, import_type, None) for attr in self.attributes]

        # flatten
        imports = [imp for sublist in imports for imp in cast(list[str], sublist)]

        # remove nulls
        imports = [imp for imp in imports if imp is not None]

        # uniq
        imports = list(set(imports))

        # sort
        imports.sort()

        # remove deplicate
        if self.name in imports:
            imports.remove(self.name)

        return cast(list[str], imports)


def filter_models_classes(klass: object) -> bool:
    """Filter out classes that don't belong to models module."""
    try:
        check = klass.__module__.startswith(KUBERNETES_CLIENT_PREFIX)
    except AttributeError:
        check = False

    return check


def generate_dicts(client_dir: Path, models_dir: Path) -> None:
    """Generate TypedDict for kubernetes models."""
    model_classes = inspect.getmembers(kubernetes_client, filter_models_classes)

    models: List[Model] = []

    for name, klass in model_classes:
        models.append(Model(name, klass))

    loader = FileSystemLoader(searchpath=DICT_CLIENT_TEMPLATE_DIRECTORY)
    library = Environment(loader=loader, autoescape=True)

    template = library.get_template("__init__.py.j2")

    init_definition = template.render(models=models)

    if client_dir.exists():
        shutil.rmtree(client_dir)

    os.makedirs(client_dir)
    with open(client_dir / "__init__.py", "w+") as codegen_file:
        codegen_file.write(init_definition)

    os.makedirs(models_dir)
    with open(models_dir / "__init__.py", "w+") as codegen_file:
        codegen_file.write(init_definition)

    for model in models:
        template = library.get_template("class.py.j2")

        klass_definition = template.render(model=model)

        with open(models_dir / "{0}.py".format(model.module_name), "w+") as codegen_file:
            codegen_file.write(klass_definition)

    comment_codegen(client_dir, "typeddictgen")
    format_codegen(client_dir)


if __name__ == "__main__":
    generate_dicts(DICT_CLIENT_DIRECTORY, DICT_CLIENT_MODELS_DIRECTORY)
