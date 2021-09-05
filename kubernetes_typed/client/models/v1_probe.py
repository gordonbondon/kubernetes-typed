# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ProbeDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ExecActionDict, V1HTTPGetActionDict, V1TCPSocketActionDict

V1ProbeDict = TypedDict(
    "V1ProbeDict",
    {
        "exec": V1ExecActionDict,
        "failureThreshold": int,
        "httpGet": V1HTTPGetActionDict,
        "initialDelaySeconds": int,
        "periodSeconds": int,
        "successThreshold": int,
        "tcpSocket": V1TCPSocketActionDict,
        "timeoutSeconds": int,
    },
    total=False,
)
