from typing import TYPE_CHECKING

from kubernetes import client

container = client.V1Container(name="pi", image="perl")

temporary = container.name

container.command = ["perl"]

info = client.V1UserInfo(extra={"extrafield1": ["extravalue1", "extravalue2"]})

if TYPE_CHECKING:
    reveal_type(temporary)
    reveal_type(container.command)
    reveal_type(info.extra)

container.command = "test"
