from functools import partial
from typing import Callable, Optional, Union

import kubernetes.client as kubernetes_client
from mypy.checker import TypeChecker
from mypy.nodes import TypeAlias, TypeInfo
from mypy.plugin import AttributeContext, Plugin
from mypy.semanal import SemanticAnalyzer
from mypy.types import AnyType, Instance
from mypy.types import Type as MypyType
from mypy.types import TypeOfAny


class KubernetesPlugin(Plugin):
    """Provides support for Kubernetes client types."""

    KUBERNETES_CLIENT_PREFIX = "kubernetes.client.models."
    OPENAPI_ATTRIBUTE = "openapi_types"

    # def get_type_analyze_hook(self, fullname: str) -> Optional[Callable]:
    #     if fullname.startswith(self.KUBERNETES_CLIENT_PREFIX):
    #         print("get_type_analyze_hook: " + fullname)
    #         return None

    #     return None

    def get_attribute_hook(self, fullname: str) -> Optional[Callable[[AttributeContext], MypyType]]:
        if fullname.startswith(self.KUBERNETES_CLIENT_PREFIX):
            class_path, _, attr_name = fullname.rpartition(".")

            _, _, class_name = class_path.rpartition(".")

            klass = getattr(kubernetes_client, class_name, None)

            if klass is None:
                return None

            oapi = getattr(klass, self.OPENAPI_ATTRIBUTE)

            return partial(attribute_callback, name=oapi[attr_name])

        return None

    # def get_dynamic_class_hook(self, fullname: str) -> Optional[Callable[[DynamicClassDefContext], None]]:
    #     if fullname.startswith(self.KUBERNETES_CLIENT_PREFIX):
    #         print("get_dynamic_class_hook: " + fullname)
    #         class_name, _, _ = fullname.rpartition(".")

    #         print(class_name)
    #         return None

    #     return None


def attribute_callback(ctx: AttributeContext, name: str) -> MypyType:
    typ = get_type(ctx.api, name)

    if typ is None:
        return AnyType(TypeOfAny.implementation_artifact)

    return typ


def get_type(api: Union[TypeChecker, SemanticAnalyzer], name: str) -> Optional[Instance]:
    if name.find("(") != -1 or name.find("[") != -1:
        return get_generic_type(api, name)

    try:
        typ = api.named_type("builtins.{}".format(name))
        return typ
    except KeyError:
        pass

    try:
        type_class = getattr(kubernetes_client, name, None)

        if type_class is None:
            return None

        # ref: mypy.checker.lookup_qualified
        n = api.modules[type_class.__module__]
        sym = n.names[type_class.__qualname__]

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


def get_generic_type(api: Union[TypeChecker, SemanticAnalyzer], name: str) -> Optional[Instance]:
    """Parse generic type definition from type hint string

    For example list[str], dict(str, str), etc.
    """

    # TODO: pretty sure this is implemented somewhere inside mypy, byt I was not able to find it
    open: str = ""
    close: str = ""

    square = name.find("[")
    round = name.find("(")

    if square != -1 and round != -1:
        if square < round:
            open = "["
            close = "]"
        elif round < square:
            open = "("
            close = ")"

    if square != -1:
        open = "["
        close = "]"
    elif round != -1:
        open = "("
        close = ")"

    type_name = name.split(open)[0]

    args = name[name.find(open) + 1 : name.rfind(close)].split(",")

    return api.named_generic_type(type_name, [get_type(api, arg) for arg in args])


def plugin(_version: str):
    return KubernetesPlugin
