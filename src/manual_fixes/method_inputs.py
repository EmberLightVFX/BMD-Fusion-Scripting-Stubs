method_inputs_to_fix: dict[str, dict[str, dict[str, str | None | list[str]]]] = {
    "Composition": {
        "Copy": {
            "input_name": "toollist",
            "old_input_type": "dict[Any, Any]",
            "input_type": "list[Tool]",
            "extra_import": "Tool",
        },
        "CopySettings": {
            "input_name": "toollist",
            "old_input_type": "dict[Any, Any]",
            "input_type": "list[Tool]",
            "extra_import": "Tool",
        },
        "Render": {
            "input_name": "settings",
            "old_input_type": "dict[Any, Any]",
            "input_type": "dict[Any, Any] | None = None",
            "extra_import": None,
        },
        "SetActiveTool": {
            "input_name": "tool",
            "old_input_type": "Tool",
            "input_type": "Tool = Tool()",
            "extra_import": None,
        },
    },
    "FlowView": {
        "SetPos": {
            "input_name": "tool",
            "old_input_type": "object",
            "input_type": "Tool",
            "extra_import": "Tool",
        },
        "GetPosTable": {
            "input_name": "tool",
            "old_input_type": "object",
            "input_type": "Tool",
            "extra_import": "Tool",
        },
        "GetPos": {
            "input_name": "Tool",
            "old_input_type": "object",
            "input_type": "Tool",
            "extra_import": "Tool",
        },
        "Select": {
            "input_name": "tool",
            "old_input_type": "object",
            "input_type": "Tool",
            "extra_import": "Tool",
        },
        "QueueSetPos": {
            "input_name": "tool",
            "old_input_type": "object",
            "input_type": "Tool",
            "extra_import": "Tool",
        },
    },
    "MailMessage": {
        "AddRecipients": {
            "input_name": "addresses",
            "old_input_type": "dict[Any, Any]",
            "input_type": "list[str]",
            "extra_import": None,
        }
    },
    "FuView": {
        "AddView": {
            "input_name": "Side",
            "old_input_type": "str",
            "input_type": 'Literal["left", "right", "above", "below"]',
            "extra_import": "Literal",
        }
    },
}
