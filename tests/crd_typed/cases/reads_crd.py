from typing import TYPE_CHECKING

from crd_typed import CustomResource

resource: CustomResource["tests/crd_typed/cases/reads_crd.yaml"]

if TYPE_CHECKING:
    reveal_type(resource)

resource["spec"]["cronSpec"] = 1
resource["spec"]["replicas"] = "1"
