# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V2alpha1CronJobSpecDict, V2alpha1CronJobStatusDict

V2alpha1CronJobDict = TypedDict(
    "V2alpha1CronJobDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V2alpha1CronJobSpecDict,
        "status": V2alpha1CronJobStatusDict,
    },
    total=False,
)
