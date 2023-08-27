"""
Make sure that the class_name and extra_import does NOT include the traling "_"!!!
"""

method_return_types_to_fix: dict[str, dict[str, dict[str, str | None]]] = {
    "ChildFrame": {
        "GetControlViewList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[FuView_]",
            "extra_import": "FuView",
        },
        "GetMainViewList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[FuView_]",
            "extra_import": "FuView",
        },
    },
    "Composition": {
        "GetCompPathMap": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[str, str]",
            "extra_import": None,
        },
        "MapPathSegments": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[str, str]",
            "extra_import": None,
        },
        "GetToolList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[int, Tool_]",
            "extra_import": "Tool",
        },
    },
    "FlowView": {
        "GetBookmarkList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[str]",
            "extra_import": None,
        }
    },
    "GLView": {
        "GetViewerList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Any]",
            "extra_import": None,
        }
    },
    "Operator": {
        "GetChildrenList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Tool_]",
            "extra_import": "Tool",
        },
        "GetOutputList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[Any, Tool_]",
            "extra_import": "Tool",
        },
        "GetInputList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[Any, Tool_]",
            "extra_import": "Tool",
        },
    },
    "PlainOutput": {
        "GetDoD": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[int] | None",
            "extra_import": None,
        },
    },
    "QueueManager": {
        "GetGroupList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Any]",
            "extra_import": None,
        },
        "GetJobList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Any]",
            "extra_import": None,
        },
        "GetRenderNodeList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Any]",
            "extra_import": None,
        },
    },
    "RenderJob": {
        "GetFailedSlaves": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Any]",
            "extra_import": None,
        }
    },
}
