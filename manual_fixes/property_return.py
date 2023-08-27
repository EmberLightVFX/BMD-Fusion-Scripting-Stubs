"""
Make sure that the class_name and extra_import does NOT include the traling "_"!!!
"""

property_return_types_to_fix: dict[str, dict[str, dict[str, str | None]]] = {
    "Image": {
        "DataWindow": {
            "return_type": "list[int]",
            "extra_import": None,
        },
    },
}
