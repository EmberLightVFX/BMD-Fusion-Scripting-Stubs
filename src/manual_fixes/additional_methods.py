from typing import Any


additional_methods_list: dict[str, Any] = {
    "Composition": [
        {
            "LongHelp": "Composition:GetAttrs(string attribute_name)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "number|string|boolean|table",
                            "Name": "attribute_value",
                        }
                    ],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "string",
                            "Name": "attribute_name",
                        }
                    ],
                },
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "table",
                            "Name": "all_attributes",
                        }
                    ],
                    "Args": [],
                },
            ],
            "Description": [
                {
                    "Text": "You can get all attributes by not passing anything",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "GetAttrs",
            "ShortHelp": "Returns the content of an attributes",
        },
        {
            "LongHelp": "Composition:SetAttrs(table attributes)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "table",
                            "Name": "attributes",
                        }
                    ],
                }
            ],
            "Description": [
                {
                    "Text": "",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "SetAttrs",
            "ShortHelp": "Set the content of an attributes",
        },
    ],
    "Fusion": [
        {
            "LongHelp": "Fusion:GetAttrs(string attribute_name)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "number|string|boolean|table",
                            "Name": "attribute_value",
                        }
                    ],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "string",
                            "Name": "attribute_name",
                        }
                    ],
                },
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "table",
                            "Name": "all_attributes",
                        }
                    ],
                    "Args": [],
                },
            ],
            "Description": [
                {
                    "Text": "You can get all attributes by not passing anything",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "GetAttrs",
            "ShortHelp": "Returns the content of an attributes",
        },
        {
            "LongHelp": "Fusion:SetAttrs(table attributes)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "table",
                            "Name": "attributes",
                        }
                    ],
                }
            ],
            "Description": [
                {
                    "Text": "Set the content of an attributes",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "SetAttrs",
            "ShortHelp": "Set the content of an attributes",
        },
    ],
    "Operator": [
        {
            "LongHelp": "Operator:GetAttrs(string attribute_name)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "number|string|boolean|table",
                            "Name": "attribute_value",
                        }
                    ],
                    "Args": [
                        {"Optional": True, "Type": "string", "Name": "attribute_name"}
                    ],
                },
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "table",
                            "Name": "all_attributes",
                        }
                    ],
                    "Args": [],
                },
            ],
            "Description": [
                {
                    "Text": "You can get all attributes by not passing anything",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "GetAttrs",
            "ShortHelp": "Returns the content of an attributes",
        },
        {
            "LongHelp": "Operator:SetAttrs(table attributes)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "table",
                            "Name": "attributes",
                        }
                    ],
                }
            ],
            "Description": [
                {
                    "Text": "",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "SetAttrs",
            "ShortHelp": "Set the content of an attributes",
        },
        {
            "LongHelp": "Operator:__getitem__(string key)\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {"Type": "number|string|boolean|table", "Name": "value"}
                    ],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "string",
                            "Name": "key",
                        }
                    ],
                }
            ],
            "Description": [
                {
                    "Text": "",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "__getitem__",
            "ShortHelp": "",
        },
    ],
    "PlainOutput": [
        {
            "LongHelp": "PlainOutput:GetTool()\n\n",
            "Type": "Function",
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "Tool",
                            "Name": "tool",
                        }
                    ],
                    "Args": [],
                }
            ],
            "Description": [
                {
                    "Text": "You can get all attributes by not passing anything",
                    "Type": "Body",
                }
            ],
            "SeeAlso": [],
            "Name": "GetTool",
            "ShortHelp": "Get the tool that the output is pointing to",
        }
    ],
}
