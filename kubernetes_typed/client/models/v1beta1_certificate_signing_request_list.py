# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CertificateSigningRequestListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequestDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V1beta1CertificateSigningRequestListDict = TypedDict(
    "V1beta1CertificateSigningRequestListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1CertificateSigningRequestDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
