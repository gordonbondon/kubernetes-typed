from typing import TYPE_CHECKING

from crd_typed import CustomResourceSpec

resource: CustomResourceSpec["tests/crd_typed/cases/reads_crd.yaml"]

if TYPE_CHECKING:
    reveal_type(resource)

# resource.myvar = 12
# resource.blabla = 12
resource["cronSpec"] = "asdsad"
