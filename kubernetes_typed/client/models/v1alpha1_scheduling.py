# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, Dict, List


from kubernetes_typed.client import V1TolerationDict

V1alpha1SchedulingDict = TypedDict(
    "V1alpha1SchedulingDict",
    {
        "nodeSelector": Dict[str, str],
        "tolerations": List[V1TolerationDict],
    },
    total=False,
)