from typing import TYPE_CHECKING

from crd_typed import CustomResource

nested_object: CustomResource["tests/crd_typed/cases/nested_crd.yaml", "spec", "internalObject"]
array: CustomResource["tests/crd_typed/cases/nested_crd.yaml", "spec", "internalArray"]
nested_array_item: CustomResource["tests/crd_typed/cases/nested_crd.yaml", "spec", "internalArray", "items"]

if TYPE_CHECKING:
    reveal_type(nested_object)
    reveal_type(array)
    reveal_type(nested_array_item)

nested_object["stringProperty"] = 1
nested_array_item["integerProperty"] = "1"
