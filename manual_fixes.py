"""
Make sure that the class_name and extra_import does NOT include the traling "_"!!!
"""

method_return_types_to_fix = [
    {
        "class_name": "ChildFrame",
        "data": [
            {
                "obj_name": "GetControlViewList",
                "return_type": "list[FuView_]",
                "extra_import": "FuView",
            },
            {
                "obj_name": "GetMainViewList",
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
                "return_type": "dict[str, str]",
                "extra_import": None,
            },
            {
                "obj_name": "MapPathSegments",
                "return_type": "dict[str, str]",
                "extra_import": None,
            },
            {
                "obj_name": "GetToolList",
                "return_type": "list[Tool_]",
                "extra_import": "Tool",
            },
        ],
    },
    {
        "class_name": "FlowView",
        "data": [
            {
                "obj_name": "GetBookmarkList",
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
                "return_type": "list[Any]",
                "extra_import": None,
            },
            {
                "obj_name": "GetJobList",
                "return_type": "list[Any]",
                "extra_import": None,
            },
            {
                "obj_name": "GetRenderNodeList",
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
    }
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


def fixMethodInputTypes(
    class_name: str, obj_name: str, input_name: str, old_input_type: str,
) -> tuple[str, str] | tuple[None, None]:
    for type_ in method_inputs_to_fix:
        if type_["class_name"] == class_name:
            for data_ in type_["data"]:
                if data_["obj_name"] == obj_name:
                    for input_ in data_["inputs"]:
                        if input_["input_name"] == input_name and input_["old_input_type"] == old_input_type:
                            return input_["input_type"], input_["extra_import"]
    return None, None  # Return a default value if no match is found


def fixMethodReturnTypes(
    class_name: str, obj_name: str
) -> tuple[str, str] | tuple[None, None]:
    for type_ in method_return_types_to_fix:
        if type_["class_name"] == class_name:
            for data_ in type_["data"]:
                if data_["obj_name"] == obj_name:
                    return data_["return_type"], data_["extra_import"]
    return None, None  # Return a default value if no match is found

def fixPropertyReturnTypes(
    class_name: str, obj_name: str
) -> tuple[str, str] | tuple[None, None]:
    for type_ in property_return_types_to_fix:
        if type_["class_name"] == class_name:
            for data_ in type_["data"]:
                if data_["obj_name"] == obj_name:
                    return data_["return_type"], data_["extra_import"]
    return None, None  # Return a default value if no match is found