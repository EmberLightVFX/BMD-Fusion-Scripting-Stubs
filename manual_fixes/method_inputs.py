"""
Make sure that the class_name and extra_import does NOT include the traling "_"!!!
"""

method_inputs_to_fix: dict[str, dict[str, dict[str, str | None]]] = {
    "Composition": {
        "Copy": {
            "input_name": "toollist",
            "old_input_type": "dict[Any, Any]",
            "input_type": "list[Tool_]",
            "extra_import": "Tool",
        },
        "CopySettings": {
            "input_name": "toollist",
            "old_input_type": "dict[Any, Any]",
            "input_type": "list[Tool_]",
            "extra_import": "Tool",
        },
        "Render": {
            "input_name": "settings",
            "old_input_type": "dict[Any, Any]",
            "input_type": "dict[Any, Any] = dict[Any, Any]()",
            "extra_import": None,
        },
        "SetActiveTool": {
            "input_name": "tool",
            "old_input_type": "Tool_",
            "input_type": "Tool_ = Tool_()",
            "extra_import": None,
        },
    },
    "FlowView": {
        "SetPos": {
            "input_name": "tool",
            "old_input_type": "object_",
            "input_type": "Tool_",
            "extra_import": "Tool",
        },
        "GetPosTable": {
            "input_name": "tool",
            "old_input_type": "object_",
            "input_type": "Tool_",
            "extra_import": "Tool",
        },
        "GetPos": {
            "input_name": "Tool",
            "old_input_type": "object_",
            "input_type": "Tool_",
            "extra_import": "Tool",
        },
        "Select": {
            "input_name": "tool",
            "old_input_type": "object_",
            "input_type": "Tool_",
            "extra_import": "Tool",
        },
        "QueueSetPos": {
            "input_name": "tool",
            "old_input_type": "object_",
            "input_type": "Tool_",
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
}

