# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

V1ContainerPortDict = TypedDict(
    "V1ContainerPortDict",
    {
        "containerPort": int,
        "hostIP": str,
        "hostPort": int,
        "name": str,
        "protocol": str,
    },
    total=False,
)