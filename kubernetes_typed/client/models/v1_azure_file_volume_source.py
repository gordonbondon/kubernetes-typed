# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1AzureFileVolumeSourceDict generated type."""
from typing import TypedDict

V1AzureFileVolumeSourceDict = TypedDict(
    "V1AzureFileVolumeSourceDict",
    {
        "readOnly": bool,
        "secretName": str,
        "shareName": str,
    },
    total=False,
)
