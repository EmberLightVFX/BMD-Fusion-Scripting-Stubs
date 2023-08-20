"""
Make sure that the class_name and extra_import does NOT include the traling "_"!!!
"""

method_return_types_to_fix = [
    {
        "class_name": "ChildFrame",
        "data": [
            {
                "obj_name": "GetControlViewList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[FuView_]",
                "extra_import": "FuView",
            },
            {
                "obj_name": "GetMainViewList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[FuView_]",
                "extra_import": "FuView",
            },
        ],
    },
    {
        "class_name": "Composition",
        "data": [
            {
                "obj_name": "GetCompPathMap",
                "old_return_type": "dict[Any, Any]",
                "return_type": "dict[str, str]",
                "extra_import": None,
            },
            {
                "obj_name": "MapPathSegments",
                "old_return_type": "dict[Any, Any]",
                "return_type": "dict[str, str]",
                "extra_import": None,
            },
            {
                "obj_name": "GetToolList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "dict[int, Tool_]",
                "extra_import": "Tool",
            },
        ],
    },
    {
        "class_name": "FlowView",
        "data": [
            {
                "obj_name": "GetBookmarkList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[str]",
                "extra_import": None,
            },
        ],
    },
    {
        "class_name": "GLView",
        "data": [
            {
                "obj_name": "GetViewerList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[Any]",
                "extra_import": None,
            },
        ],
    },
    {
        "class_name": "Operator",
        "data": [
            {
                "obj_name": "GetChildrenList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[Tool_]",
                "extra_import": "Tool",
            },
        ],
    },
    {
        "class_name": "Operator",
        "data": [
            {
                "obj_name": "GetOutputList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "dict[Any, Tool_]",
                "extra_import": "Tool",
            },
        ],
    },
    {
        "class_name": "Operator",
        "data": [
            {
                "obj_name": "GetInputList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "dict[Any, Tool_]",
                "extra_import": "Tool",
            },
        ],
    },
    {
        "class_name": "PlainOutput",
        "data": [
            {
                "obj_name": "GetDoD",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[int] | None",
                "extra_import": None,
            },
        ],
    },
    {
        "class_name": "QueueManager",
        "data": [
            {
                "obj_name": "GetGroupList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[Any]",
                "extra_import": None,
            },
            {
                "obj_name": "GetJobList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[Any]",
                "extra_import": None,
            },
            {
                "obj_name": "GetRenderNodeList",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[Any]",
                "extra_import": None,
            },
        ],
    },
    {
        "class_name": "RenderJob",
        "data": [
            {
                "obj_name": "GetFailedSlaves",
                "old_return_type": "dict[Any, Any]",
                "return_type": "list[Any]",
                "extra_import": None,
            },
        ],
    },
]

method_inputs_to_fix = [
    {
        "class_name": "Composition",
        "data": [
            {
                "obj_name": "Copy",
                "inputs": [
                    {
                        "input_name": "toollist",
                        "old_input_type": "dict[Any, Any]",
                        "input_type": "list[Tool_]",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "CopySettings",
                "inputs": [
                    {
                        "input_name": "toollist",
                        "old_input_type": "dict[Any, Any]",
                        "input_type": "list[Tool_]",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "Render",
                "inputs": [
                    {
                        "input_name": "settings",
                        "old_input_type": "dict[Any, Any]",
                        "input_type": "dict[Any, Any] = dict[Any, Any]()",
                        "extra_import": None,
                    }
                ],
            },
            {
                "obj_name": "SetActiveTool",
                "inputs": [
                    {
                        "input_name": "tool",
                        "old_input_type": "Tool_",
                        "input_type": "Tool_ = Tool_()",
                        "extra_import": None,
                    }
                ],
            },
        ],
    },
    {
        "class_name": "FlowView",
        "data": [
            {
                "obj_name": "GetPos",
                "inputs": [
                    {
                        "input_name": "Tool",
                        "old_input_type": "object_",
                        "input_type": "Tool_",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "SetPos",
                "inputs": [
                    {
                        "input_name": "tool",
                        "old_input_type": "object_",
                        "input_type": "Tool_",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "GetPosTable",
                "inputs": [
                    {
                        "input_name": "tool",
                        "old_input_type": "object_",
                        "input_type": "Tool_",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "GetPos",
                "inputs": [
                    {
                        "input_name": "tool",
                        "old_input_type": "object_",
                        "input_type": "Tool_",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "Select",
                "inputs": [
                    {
                        "input_name": "tool",
                        "old_input_type": "object_",
                        "input_type": "Tool_",
                        "extra_import": "Tool",
                    }
                ],
            },
            {
                "obj_name": "QueueSetPos",
                "inputs": [
                    {
                        "input_name": "tool",
                        "old_input_type": "object_",
                        "input_type": "Tool_",
                        "extra_import": "Tool",
                    }
                ],
            },
        ],
    },
    {
        "class_name": "MailMessage",
        "data": [
            {
                "obj_name": "AddRecipients",
                "inputs": [
                    {
                        "input_name": "addresses",
                        "old_input_type": "dict[Any, Any]",
                        "input_type": "list[str]",
                        "extra_import": None,
                    }
                ],
            },
        ],
    },
]

property_return_types_to_fix = [
    {
        "class_name": "Image",
        "data": [
            {
                "obj_name": "DataWindow",
                "return_type": "list[int]",
                "extra_import": None,
            },
        ],
    },
]


def fixInputTypes(
    class_name: str,
    obj_name: str,
    input_name: str,
    old_input_type: str,
) -> tuple[str, str]:
    for type_ in method_inputs_to_fix:
        if type_["class_name"] == class_name:
            for data_ in type_["data"]:
                if data_["obj_name"] == obj_name:
                    for input_ in data_["inputs"]:
                        if (
                            input_["input_name"] == input_name
                            and input_["old_input_type"] == old_input_type
                        ):
                            return input_["input_type"], input_["extra_import"]
    return "", ""  # Return a default value if no match is found


def fixMethodReturnTypes(
    class_name: str,
    obj_name: str,
    old_return_type: str,
) -> tuple[str, str]:
    for type_ in method_return_types_to_fix:
        if type_["class_name"] == class_name:
            for data_ in type_["data"]:
                if (
                    data_["obj_name"] == obj_name
                    and data_["old_return_type"] == old_return_type
                ):
                    return data_["return_type"], data_["extra_import"]
    return "", ""  # Return a default value if no match is found


def fixPropertyReturnTypes(class_name: str, obj_name: str) -> tuple[str, str]:
    for type_ in property_return_types_to_fix:
        if type_["class_name"] == class_name:
            for data_ in type_["data"]:
                if data_["obj_name"] == obj_name:
                    return data_["return_type"], data_["extra_import"]
    return "", ""  # Return a default value if no match is found
