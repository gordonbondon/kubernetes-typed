# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


V1beta1PolicyRuleDict = TypedDict(
    "V1beta1PolicyRuleDict",
    {
        "apiGroups": List[str],
        "nonResourceURLs": List[str],
        "resourceNames": List[str],
        "resources": List[str],
        "verbs": List[str],
    },
    total=False,
)