method_return_types_to_fix: dict[str, dict[str, dict[str, str | list[str] | None]]] = {
    "ChildFrame": {
        "GetControlViewList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[FuView]",
            "extra_import": "FuView",
        },
        "GetMainViewList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[FuView]",
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
            "return_type": "dict[int, Tool]",
            "extra_import": "Tool",
        },
        "ChooseTool": {
            "old_return_type": "str | str",
            "return_type": "str | tuple[str, str]",
            "extra_import": None,
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
        "FindMainInput": {
            "old_return_type": "Input",
            "return_type": "PlainInput",
            "extra_import": "PlainInput",
        },
        "GetChildrenList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "list[Tool]",
            "extra_import": "Tool",
        },
        "GetOutputList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[Any, Tool]",
            "extra_import": "Tool",
        },
        "GetInputList": {
            "old_return_type": "dict[Any, Any]",
            "return_type": "dict[Any, Tool]",
            "extra_import": "Tool",
        },
        "Refresh": {
            "old_return_type": "None",
            "return_type": "Tool",
            "extra_import": "Tool",
        },
    },
    "PlainInput": {
        "GetConnectedOutput": {
            "old_return_type": "Output",
            "return_type": "PlainOutput | None",
            "extra_import": "PlainOutput",
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
