# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, Dict


ExtensionsV1beta1ScaleStatusDict = TypedDict(
    "ExtensionsV1beta1ScaleStatusDict",
    {
        "replicas": int,
        "selector": Dict[str, str],
        "targetSelector": str,
    },
    total=False,
)