# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceSubresourcesDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1CustomResourceSubresourceScaleDict

V1CustomResourceSubresourcesDict = TypedDict(
    "V1CustomResourceSubresourcesDict",
    {
        "scale": V1CustomResourceSubresourceScaleDict,
        "status": object,
    },
    total=False,
)
