additional_methods_list = {
    "Composition": {
        "GetAttrs": {
            "short_help": "Returns the content of an attributes",
            "description": "You can get all attributes by not passing anything",
            "usage": [
                "(number|string|boolean|table) :GetAttrs(string attribute_name)",
                "table :GetAttrs()",
            ],
        },
        "SetAttrs": {
            "short_help": "Set the content of an attributes",
            "description": "",
            "usage": [" :SetAttrs(table attributes)"],
        },
    },
    "Fusion": {
        "GetAttrs": {
            "short_help": "Returns the content of an attributes",
            "description": "You can get all attributes by not passing anything",
            "usage": [
                "(number|string|boolean|table) :GetAttrs(string attribute_name)",
                "table :GetAttrs()",
            ],
        },
        "SetAttrs": {
            "short_help": "Set the content of an attributes",
            "description": "",
            "usage": [" :SetAttrs(table attributes)"],
        },
    },
    "Operator": {
        "GetAttrs": {
            "short_help": "Returns the content of an attributes",
            "description": "You can get all attributes by not passing anything",
            "usage": [
                "(number|string|boolean|table) :GetAttrs(string attribute_name)",
                "table :GetAttrs()",
            ],
        },
        "SetAttrs": {
            "short_help": "Set the content of an attributes",
            "description": "",
            "usage": [" :SetAttrs(table attributes)"],
        },
        "__getitem__": {
            "usage": ["(number|string|boolean|table) :__getitem__(string key)"],
        }
    },
    "PlainOutput": {
        "GetTool": {
            "short_help": "Get the tool that the output is pointing to",
            "description": "You can get all attributes by not passing anything",
            "usage": [
                "Tool :GetTool()",
            ],
        },
    },
}
