# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1EventDict generated type."""
import datetime
from typing import TypedDict

from kubernetes_typed.client import V1EventSourceDict, V1ObjectMetaDict, V1ObjectReferenceDict, V1beta1EventSeriesDict

V1beta1EventDict = TypedDict(
    "V1beta1EventDict",
    {
        "action": str,
        "apiVersion": str,
        "deprecatedCount": int,
        "deprecatedFirstTimestamp": datetime.datetime,
        "deprecatedLastTimestamp": datetime.datetime,
        "deprecatedSource": V1EventSourceDict,
        "eventTime": datetime.datetime,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "note": str,
        "reason": str,
        "regarding": V1ObjectReferenceDict,
        "related": V1ObjectReferenceDict,
        "reportingController": str,
        "reportingInstance": str,
        "series": V1beta1EventSeriesDict,
        "type": str,
    },
    total=False,
)
