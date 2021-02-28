from typing import TYPE_CHECKING

from kubernetes import client

container = client.V1Container(name="pi", image="perl")

temporary = container.name

container.command = ["perl"]

if TYPE_CHECKING:
    reveal_type(temporary)
    reveal_type(container.command)

container.command = "test"
