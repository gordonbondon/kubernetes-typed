# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

V1beta1CSIDriverSpecDict = TypedDict(
    "V1beta1CSIDriverSpecDict",
    {
        "attachRequired": bool,
        "podInfoOnMount": bool,
        "volumeLifecycleModes": List[str],
    },
    total=False,
)