# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ExecActionDict, V1HTTPGetActionDict, V1TCPSocketActionDict

V1HandlerDict = TypedDict(
    "V1HandlerDict",
    {
        "exec": V1ExecActionDict,
        "httpGet": V1HTTPGetActionDict,
        "tcpSocket": V1TCPSocketActionDict,
    },
    total=False,
)
