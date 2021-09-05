"""plugin implements mypy plugin."""
from functools import partial
from types import MappingProxyType
from typing import Any, Callable, List, Optional, Tuple

from kubernetes import client as kubernetes_client
from mypy.checker import TypeChecker
from mypy.nodes import MypyFile, TypeAlias, TypeInfo
from mypy.plugin import AttributeContext, CallableType, FunctionSigContext, Plugin
from mypy.types import AnyType, Instance, NoneType
from mypy.types import Type as MypyType
from mypy.types import TypeOfAny, UnionType

KUBERNETES_CLIENT_PREFIX = "kubernetes.client.models."
OPENAPI_ATTRIBUTE = "openapi_types"
ATTRIBUTE_NAME_ATTRIBUTE = "attribute_map"
NATIVE_TYPES_MAPPING = kubernetes_client.ApiClient.NATIVE_TYPES_MAPPING

BRACKET_SQUARE = "["
BRACKET_ROUND = "("
BRACKET_CLOSING = MappingProxyType(
    {
        BRACKET_SQUARE: "]",
        BRACKET_ROUND: ")",
    },
)


class KubernetesPlugin(Plugin):
    """Provides support for Kubernetes client types."""

    def get_attribute_hook(self, fullname: str) -> Optional[Callable[[AttributeContext], MypyType]]:
        """Get attribute hook callback."""
        if fullname.startswith(KUBERNETES_CLIENT_PREFIX):
            class_path, _, attr_name = fullname.rpartition(".")

            _, _, class_name = class_path.rpartition(".")

            name = get_model_openapi_type_name(class_name, attr_name)
            if name is None:
                return None

            return partial(attribute_callback, name=name)

        return None

    def get_function_signature_hook(self, fullname: str) -> Optional[Callable[[FunctionSigContext], CallableType]]:
        """Get function hook callback."""
        if fullname.startswith(KUBERNETES_CLIENT_PREFIX):
            return function_signature_callback

        return None

    def get_additional_deps(self, _: MypyFile) -> List[Tuple[int, str, int]]:
        """Add ``datetime`` as a dependency, required by NATIVE_TYPES_MAPPING."""
        return [(10, "datetime", -1)]


def function_signature_callback(ctx: FunctionSigContext) -> CallableType:
    """Call Function callback."""
    assert isinstance(ctx.api, TypeChecker)

    signature = ctx.default_signature

    try:
        new_arg_types: List[MypyType] = [
            UnionType([AnyType(TypeOfAny.implementation_artifact), NoneType()]) for _ in enumerate(signature.arg_names)
        ]

        for i, _ in enumerate(signature.arg_names):
            arg_name = signature.arg_names[i]

            if arg_name is None:
                continue

            _, _, class_name = "{0}".format(signature.ret_type).rpartition(".")

            type_name = get_model_openapi_type_name(class_name, arg_name)

            if type_name is None:
                continue

            typ = get_attribute_type(ctx.api, type_name)

            if isinstance(typ, MypyType):
                new_arg_types[i] = UnionType([typ, NoneType()])

        signature.arg_types = new_arg_types

        return signature
    except KeyError:
        return signature


def attribute_callback(ctx: AttributeContext, name: str) -> MypyType:
    """Attribute callback."""
    assert isinstance(ctx.api, TypeChecker)

    typ = get_attribute_type(ctx.api, name)

    if typ is None:
        return AnyType(TypeOfAny.implementation_artifact)

    return typ


def get_attribute_type(api: TypeChecker, name: str) -> Optional[Instance]:
    """Get type definition of an attribute."""
    if name.find("(") != -1 or name.find("[") != -1:
        return get_generic_type(api, name)

    native = NATIVE_TYPES_MAPPING.get(name)
    if native is not None:
        return api.named_type("{0}.{1}".format(native.__module__, native.__qualname__))

    try:
        klass = getattr(kubernetes_client, name, None)

        if klass is None:
            return None

        # From mypy.checker.lookup_qualified
        n = api.modules[klass.__module__]
        sym = n.names[klass.__qualname__]

        # From mypy.checker.named_type
        node = sym.node
        if isinstance(node, TypeAlias):
            assert isinstance(node.target, Instance)
            node = node.target.type
        assert isinstance(node, TypeInfo)
        any_type = AnyType(TypeOfAny.from_omitted_generics)
        return Instance(node, [any_type for _ in enumerate(node.defn.type_vars)])
    except KeyError:
        return None


def get_generic_type(api: TypeChecker, name: str) -> Optional[Instance]:
    """Parse generic type definition from type hint string.

    For example list[str], dict(str, str), etc.
    """
    # TODO: pretty sure this is implemented somewhere inside mypy, byt I was not able to find it
    start: str = ""

    square = name.find(BRACKET_SQUARE)
    paren = name.find(BRACKET_ROUND)

    if square != -1 and paren != -1:
        if square < paren:
            start = BRACKET_SQUARE
        elif paren < square:
            start = BRACKET_ROUND
    elif square != -1:
        start = BRACKET_SQUARE
    elif paren != -1:
        start = BRACKET_ROUND

    type_name = name.split(start)[0]

    args = name[name.find(start) + 1 : name.rfind(BRACKET_CLOSING[start])].split(",")

    type_args: List[MypyType] = []

    for arg in args:
        type_arg = get_attribute_type(api, arg.strip())
        if type_arg is not None:
            type_args.append(type_arg)

    return api.named_generic_type(type_name, type_args)


def get_model_openapi_type_name(class_name: str, attr_name: str) -> Optional[str]:
    """Get attribute type from openapi definition."""
    klass = getattr(kubernetes_client, class_name, None)

    if klass is None:
        return None

    oapi = getattr(klass, OPENAPI_ATTRIBUTE)

    name: str = oapi.get(attr_name)
    if name is not None:
        return name

    return None


def plugin(_version: str) -> Any:
    """Get mypy Kubernetes plugin."""
    return KubernetesPlugin
