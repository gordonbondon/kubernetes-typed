from typing import TYPE_CHECKING

from crd_typed import CustomResource

wrong_object: CustomResource["tests/crd_typed/cases/wrong_spec.yaml", "spec", "wrongObject"]
