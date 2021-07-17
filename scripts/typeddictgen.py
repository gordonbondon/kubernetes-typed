#!/usr/bin/env python3

import inspect
import os
import re
import shutil
from pathlib import Path
from typing import List

import kubernetes.client as kubernetes_client
from jinja2 import Environment, FileSystemLoader

from kubernetes_typed.plugin import (
    ATTRIBUTE_NAME_ATTRIBUTE,
    KUBERNETES_CLIENT_PREFIX,
    NATIVE_TYPES_MAPPING,
    OPENAPI_ATTRIBUTE,
)
from scripts.generate_utils import PROJECT_DIRECTORY, comment_codegen, format

DICT_CLIENT_TEMPLATE_DIRECTORY = PROJECT_DIRECTORY / "scripts" / "templates" / "typeddict"
DICT_CLIENT_DIRECTORY = PROJECT_DIRECTORY / "kubernetes_typed" / "client"
DICT_CLIENT_MODELS_DIRECTORY = DICT_CLIENT_DIRECTORY / "models"


class Attribute(object):
    """
    Represents parsed state of kubernetes client model attribute
    """

    def __init__(self, name: str, class_name: str, model_name: str) -> None:
        self.name = name
        self.class_name = class_name
        self.model_name = model_name
        self.direct_import: List[str] = []
        self.typing_import: List[str] = []
        self.model_import: List[str] = []

        self.type = self.get_type(class_name)

    def get_type(self, class_name: str) -> str:
        # ref: kubernetes.client.api_client.deserialize
        if class_name.startswith("list["):
            self.typing_import.append("List")

            sub_class_name = re.match(r"list\[(.*)\]", class_name).group(1)  # type: ignore

            typ: str = self.get_type(sub_class_name)

            return "List[{}]".format(typ)

        if class_name.startswith("dict("):
            self.typing_import.append("Dict")

            key_name = re.match(r"dict\(([^,]*), (.*)\)", class_name).group(1)  # type: ignore
            sub_class_name = re.match(r"dict\(([^,]*), (.*)\)", class_name).group(2)  # type: ignore

            key = self.get_type(key_name)
            typ = self.get_type(sub_class_name)

            return "Dict[{}, {}]".format(key, typ)

        if class_name in NATIVE_TYPES_MAPPING:
            klass = NATIVE_TYPES_MAPPING[class_name]
            module = klass.__module__

            if module == "builtins":
                typ = klass.__qualname__
                return typ
            else:
                self.direct_import.append(module)
                typ = module + "." + klass.__qualname__
                return typ

        klass = getattr(kubernetes_client, class_name, None)

        if klass is None:
            raise Exception("Attribute with missing model: {}".format(class_name))
        else:
            typ = "{}Dict".format(klass.__qualname__)
            self.model_import.append(typ)

            # recursive types not supported https://github.com/python/mypy/issues/731
            if typ == self.model_name:
                self.typing_import.append("Any")
                self.typing_import.append("Dict")
                typ = "Dict[Any, Any]"

            return typ


class Model(object):
    """
    Represents parsed state of kubernetes client model
    """

    def __init__(self, class_name: str, klass: object) -> None:
        self.class_name = class_name
        self.klass = klass

        if not filter_models_classes(klass):
            raise Exception("Incompatible module for Models class: {}".format(klass.__module__))

        self.module_full_name = klass.__module__.replace("kubernetes.", "kubernetes_typed.")
        self.module_name = klass.__module__.rpartition(".")[2]
        self.name = "{}Dict".format(class_name)

        oapi = getattr(klass, OPENAPI_ATTRIBUTE)
        attrs = getattr(klass, ATTRIBUTE_NAME_ATTRIBUTE)

        self.attributes: List[Attribute] = []

        for name, typ in oapi.items():
            self.attributes.append(Attribute(attrs[name], typ, self.name))

        self.direct_import = self.uniq_imports("direct_import")
        self.typing_import = self.uniq_imports("typing_import")
        self.model_import = self.uniq_imports("model_import")

    def uniq_imports(self, import_type: str) -> List[str]:
        # get all imports
        imports = [getattr(attr, import_type, None) for attr in self.attributes]

        # flatten
        imports = [imp for sublist in imports for imp in sublist]

        # remove nulls
        imports = [imp for imp in imports if imp is not None]

        # uniq
        imports = list(set(imports))

        # sort
        imports.sort()

        # remove deplicate
        if self.name in imports:
            imports.remove(self.name)

        return imports


def filter_models_classes(klass: object) -> bool:
    """
    Filters out classes that don't belong to models module
    """

    try:
        check = klass.__module__.startswith(KUBERNETES_CLIENT_PREFIX)
    except AttributeError:
        check = False

    return check


def generate_dicts(client_dir: Path, models_dir: Path) -> None:
    model_classes = inspect.getmembers(kubernetes_client, filter_models_classes)

    models: List[Model] = []

    for name, klass in model_classes:
        models.append(Model(name, klass))

    loader = FileSystemLoader(searchpath=DICT_CLIENT_TEMPLATE_DIRECTORY)
    library = Environment(loader=loader)

    template = library.get_template("__init__.py.j2")

    init_definition = template.render(models=models)

    if client_dir.exists():
        shutil.rmtree(client_dir)

    os.makedirs(client_dir)
    with open(client_dir / "__init__.py", "w+") as file:
        file.write(init_definition)

    os.makedirs(models_dir)
    with open(models_dir / "__init__.py", "w+") as file:
        file.write(init_definition)

    for model in models:
        template = library.get_template("class.py.j2")

        klass_definition = template.render(model=model)

        with open(models_dir / "{}.py".format(model.module_name), "w+") as file:
            file.write(klass_definition)

    comment_codegen(client_dir, "typeddictgen")
    format(client_dir, 180)


if __name__ == "__main__":
    generate_dicts(DICT_CLIENT_DIRECTORY, DICT_CLIENT_MODELS_DIRECTORY)
