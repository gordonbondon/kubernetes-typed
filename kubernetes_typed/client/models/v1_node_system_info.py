# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NodeSystemInfoDict generated type."""
from typing import TypedDict

V1NodeSystemInfoDict = TypedDict(
    "V1NodeSystemInfoDict",
    {
        "architecture": str,
        "bootID": str,
        "containerRuntimeVersion": str,
        "kernelVersion": str,
        "kubeProxyVersion": str,
        "kubeletVersion": str,
        "machineID": str,
        "operatingSystem": str,
        "osImage": str,
        "systemUUID": str,
    },
    total=False,
)
