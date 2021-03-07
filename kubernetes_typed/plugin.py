from functools import partial
from typing import Callable, Dict, List, Optional

import kubernetes.client as kubernetes_client
from mypy.checker import TypeChecker
from mypy.nodes import TypeAlias, TypeInfo
from mypy.plugin import AttributeContext, Plugin
from mypy.types import AnyType, Instance
from mypy.types import Type as MypyType
from mypy.types import TypeOfAny

KUBERNETES_CLIENT_PREFIX = "kubernetes.client.models."
OPENAPI_ATTRIBUTE = "openapi_types"
NATIVE_TYPES_MAPPING = kubernetes_client.ApiClient.NATIVE_TYPES_MAPPING


class KubernetesPlugin(Plugin):
    """Provides support for Kubernetes client types."""

    # def get_type_analyze_hook(self, fullname: str) -> Optional[Callable]:
    #     if fullname.startswith(self.KUBERNETES_CLIENT_PREFIX):
    #         print("get_type_analyze_hook: " + fullname)
    #         return None

    #     return None

    def get_attribute_hook(self, fullname: str) -> Optional[Callable[[AttributeContext], MypyType]]:
        if fullname.startswith(KUBERNETES_CLIENT_PREFIX):
            class_path, _, attr_name = fullname.rpartition(".")

            _, _, class_name = class_path.rpartition(".")

            klass = getattr(kubernetes_client, class_name, None)

            if klass is None:
                return None

            oapi = getattr(klass, OPENAPI_ATTRIBUTE)

            name = oapi.get(attr_name)
            if name is None:
                return None

            return partial(attribute_callback, name=name)

        return None

    # def get_dynamic_class_hook(self, fullname: str) -> Optional[Callable[[DynamicClassDefContext], None]]:
    #     if fullname.startswith(self.KUBERNETES_CLIENT_PREFIX):
    #         print("get_dynamic_class_hook: " + fullname)
    #         class_name, _, _ = fullname.rpartition(".")

    #         print(class_name)
    #         return None

    #     return None


def attribute_callback(ctx: AttributeContext, name: str) -> MypyType:
    assert isinstance(ctx.api, TypeChecker)
    typ = get_type(ctx.api, name)

    if typ is None:
        return AnyType(TypeOfAny.implementation_artifact)

    return typ


def get_type(api: TypeChecker, name: str) -> Optional[Instance]:
    if name.find("(") != -1 or name.find("[") != -1:
        return get_generic_type(api, name)

    try:
        klass = NATIVE_TYPES_MAPPING.get(name)

        if klass is None:
            return None

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
        type_arg = get_type(api, arg.strip())
        if type_arg is not None:
            type_args.append(type_arg)

    return api.named_generic_type(type_name, type_args)


def plugin(_version: str):
    return KubernetesPlugin
