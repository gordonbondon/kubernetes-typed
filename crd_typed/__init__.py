class CustomResource(dict):
    """Placeholder for Custom Resource body TypedDict."""

    def __class_getitem__(cls, item):
        return dict
