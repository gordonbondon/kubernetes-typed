# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1HTTPHeaderDict

V1HTTPGetActionDict = TypedDict(
    "V1HTTPGetActionDict",
    {
        "host": str,
        "httpHeaders": List[V1HTTPHeaderDict],
        "path": str,
        "port": object,
        "scheme": str,
    },
    total=False,
)