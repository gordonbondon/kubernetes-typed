import warnings
from typing import Any, Callable, Dict, List, Optional, Set, Union, cast

import yaml
from jsonschema_typed.plugin import APIv7, TypeMaker
from mypy.nodes import MDEF, CallExpr, SymbolTableNode, Var
from mypy.plugin import AnalyzeTypeContext, ClassDefContext, Plugin
from mypy.types import RawExpressionType, TypedDictType, UnboundType


class CRDPlugin(Plugin):
    """Provides support for the CRD specs as TypedDict."""

    CustomResource = "crd_typed.CustomResource"
    CustomResourceSpec = "crd_typed.CustomResourceSpec"

    def get_type_analyze_hook(self, fullname: str) -> Optional[Callable]:
        if fullname == self.CustomResource:
            return custom_resource_callback

        if fullname == self.CustomResourceSpec:
            return custom_resource_spec_callback

        return None

    def get_additional_deps(self, file):
        """Add ``mypy_extensions`` as a dependency."""
        return [(10, "mypy_extensions", -1)]


def custom_resource_callback(ctx: AnalyzeTypeContext) -> TypedDictType:
    if not ctx.type.args:
        return ctx.type

    args = list(map(resolve_arg, ctx.type.args))

    definition_path = args[0]

    openapi_schema = load_schema(definition_path)

    make_type = TypeMaker("", openapi_schema, api_version=APIv7)
    _type = make_type(ctx)


def custom_resource_spec_callback(ctx: AnalyzeTypeContext) -> TypedDictType:
    if not ctx.type.args:
        return ctx.type

    args = list(map(resolve_arg, ctx.type.args))

    definition_path = args[0]

    openapi_schema = load_schema(definition_path)

    spec_schema = openapi_schema["properties"]["spec"]

    make_type = TypeMaker("", spec_schema, api_version=APIv7)
    _type = make_type(ctx)

    return _type


def resolve_arg(value: Union[RawExpressionType, UnboundType]):
    var: str
    if isinstance(value, RawExpressionType):
        var = value.literal_value
    else:
        var = value.original_str_expr

    return var


def load_schema(path: str) -> dict:
    with open(path, "r") as stream:
        schema = yaml.safe_load(stream)["spec"]["versions"][0]["schema"]["openAPIV3Schema"]

    # provide sane name for TypeDict
    schema["title"] = "OpenAPIV3Schema"

    return schema


def plugin(_version: str):
    return CRDPlugin
