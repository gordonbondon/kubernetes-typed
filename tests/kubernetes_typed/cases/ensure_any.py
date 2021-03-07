from typing import TYPE_CHECKING

from kubernetes import client

meta = client.V1ObjectMeta(generate_name="test-")

if TYPE_CHECKING:
    # returns Any with missing satetime import
    reveal_type(meta.creation_timestamp)
