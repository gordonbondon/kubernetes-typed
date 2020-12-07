from typing import TYPE_CHECKING

from crd_typed import CustomResource

resource: CustomResource["tests/crd_typed/cases/reads_crd.yaml"]
spec: CustomResource["tests/crd_typed/cases/reads_crd.yaml", "spec"]

if TYPE_CHECKING:
    reveal_type(resource)
    reveal_type(spec)

resource["spec"]["cronSpec"] = 1
spec["replicas"] = "1"
