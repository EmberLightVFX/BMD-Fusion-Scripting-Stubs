property_return_types_to_fix: dict[str, dict[str, dict[str, str | None]]] = {
    "Image": {
        "DataWindow": {
            "return_type": "list[int]",
            "extra_import": None,
        },
    },
}
