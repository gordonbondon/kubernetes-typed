# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1NodeSelectorTermDict

V1PreferredSchedulingTermDict = TypedDict(
    "V1PreferredSchedulingTermDict",
    {
        "preference": V1NodeSelectorTermDict,
        "weight": int,
    },
    total=False,
)
