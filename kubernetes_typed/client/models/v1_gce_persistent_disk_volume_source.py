# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

V1GCEPersistentDiskVolumeSourceDict = TypedDict(
    "V1GCEPersistentDiskVolumeSourceDict",
    {
        "fsType": str,
        "partition": int,
        "pdName": str,
        "readOnly": bool,
    },
    total=False,
)