argument_names_to_fix: dict[str, dict[str, dict[str, str | None | list[str]]]] = {
    "FuView": {
        "AddView": {
            "old_arg_name": "Side:_left,_right,_above,_below",
            "new_arg_name": "Side",
        }
    },
}
