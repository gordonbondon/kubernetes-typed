from functools import partial
from typing import Callable, Dict, List, Optional, Tuple

import kubernetes.client as kubernetes_client
from mypy.checker import TypeChecker
from mypy.nodes import MypyFile, TypeAlias, TypeInfo
from mypy.plugin import AttributeContext, CallableType, FunctionSigContext, Plugin
from mypy.types import AnyType, Instance, NoneType
from mypy.types import Type as MypyType
from mypy.types import TypeOfAny, UnionType

KUBERNETES_CLIENT_PREFIX = "kubernetes.client.models."
OPENAPI_ATTRIBUTE = "openapi_types"
NATIVE_TYPES_MAPPING = kubernetes_client.ApiClient.NATIVE_TYPES_MAPPING


class KubernetesPlugin(Plugin):
    """Provides support for Kubernetes client types."""

    def get_attribute_hook(self, fullname: str) -> Optional[Callable[[AttributeContext], MypyType]]:
        if fullname.startswith(KUBERNETES_CLIENT_PREFIX):
            class_path, _, attr_name = fullname.rpartition(".")

            _, _, class_name = class_path.rpartition(".")

            name = get_model_openapi_type_name(class_name, attr_name)
            if name is None:
                return None

            return partial(attribute_callback, name=name)

        return None

    def get_function_signature_hook(self, fullname: str) -> Optional[Callable[[FunctionSigContext], CallableType]]:
        if fullname.startswith(KUBERNETES_CLIENT_PREFIX):
            return function_signature_callback

        return None

    def get_additional_deps(self, _: MypyFile) -> List[Tuple[int, str, int]]:
        """Add ``datetime`` as a dependency, required by NATIVE_TYPES_MAPPING."""
        return [(10, "datetime", -1)]


def function_signature_callback(ctx: FunctionSigContext) -> CallableType:
    assert isinstance(ctx.api, TypeChecker)

    signature = ctx.default_signature

    try:
        new_arg_types: List[MypyType] = [UnionType([AnyType(TypeOfAny.implementation_artifact), NoneType()])] * len(
            signature.arg_names
        )

        for i in range(len(signature.arg_names)):
            arg_name = signature.arg_names[i]

            if arg_name is None:
                continue

            _, _, class_name = f"{signature.ret_type}".rpartition(".")

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
    assert isinstance(ctx.api, TypeChecker)

    typ = get_attribute_type(ctx.api, name)

    if typ is None:
        return AnyType(TypeOfAny.implementation_artifact)

    return typ


def get_attribute_type(api: TypeChecker, name: str) -> Optional[Instance]:
    if name.find("(") != -1 or name.find("[") != -1:
        return get_generic_type(api, name)

    try:
        klass = NATIVE_TYPES_MAPPING[name]

        return api.named_type("{}.{}".format(klass.__module__, klass.__qualname__))
    except KeyError:
        pass

    try:
        klass = getattr(kubernetes_client, name, None)

        if klass is None:
            return None

        # ref: mypy.checker.lookup_qualified
        n = api.modules[klass.__module__]
        sym = n.names[klass.__qualname__]

        # ref: mypy.checker.named_type
        node = sym.node
        if isinstance(node, TypeAlias):
            assert isinstance(node.target, Instance)  # type: ignore
            node = node.target.type
        assert isinstance(node, TypeInfo)
        any_type = AnyType(TypeOfAny.from_omitted_generics)
        return Instance(node, [any_type] * len(node.defn.type_vars))
    except KeyError:
        pass

    return None


def get_generic_type(api: TypeChecker, name: str) -> Optional[Instance]:
    """Parse generic type definition from type hint string

    For example list[str], dict(str, str), etc.
    """

    # TODO: pretty sure this is implemented somewhere inside mypy, byt I was not able to find it
    start: str = ""
    close: Dict[str, str] = {"(": ")", "[": "]"}

    square = name.find("[")
    paren = name.find("(")

    if square != -1 and paren != -1:
        if square < paren:
            start = "["
        elif paren < square:
            start = "("
    elif square != -1:
        start = "["
    elif paren != -1:
        start = "("

    type_name = name.split(start)[0]

    args = name[name.find(start) + 1 : name.rfind(close[start])].split(",")

    type_args: List[MypyType] = []

    for arg in args:
        type_arg = get_attribute_type(api, arg.strip())
        if type_arg is not None:
            type_args.append(type_arg)

    return api.named_generic_type(type_name, type_args)


def get_model_openapi_type_name(class_name: str, attr_name: str) -> Optional[str]:
    klass = getattr(kubernetes_client, class_name, None)

    if klass is None:
        return None

    oapi = getattr(klass, OPENAPI_ATTRIBUTE)

    name = oapi.get(attr_name)

    return name


def plugin(_version: str):
    return KubernetesPlugin
