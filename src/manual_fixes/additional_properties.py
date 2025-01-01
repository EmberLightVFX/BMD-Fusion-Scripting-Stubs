from typing import Any


additional_properties_list: dict[str, Any] = {
    "Composition": [
        {
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "float",
                            "Name": "frame",
                        }
                    ],
                    "Args": [],
                }
            ],
            "Type": "Variable",
            "Description": [],
            "VarRead": True,
            "VarWrite": False,
            "LongHelp": "",
            "ShortHelp": "",
            "Name": "TIME_UNDEFINED",
            "SeeAlso": [],
        }
    ],
    "Operator": [
        {
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "dict[int,str]",
                            "Name": "Comment",
                        }
                    ],
                    "Args": [],
                },
                {
                    "Description": "",
                    "Returns": [],
                    "Args": [
                        {
                            "Optional": False,
                            "Type": "float",
                            "Name": "frame",
                        }
                    ],
                },
            ],
            "Type": "Variable",
            "Description": [
                {
                    "Text": "Access using Comments[frame/TIME_UNDEFINED]",
                    "Type": "Body",
                }
            ],
            "VarRead": True,
            "VarWrite": True,
            "LongHelp": "",
            "ShortHelp": "Access the nodes comments field.",
            "Name": "Comments",
            "SeeAlso": [],
        },
        {
            "Usage": [
                {
                    "Description": "",
                    "Returns": [
                        {
                            "Type": "string",
                            "Name": "ID",
                        }
                    ],
                    "Args": [],
                }
            ],
            "Type": "Variable",
            "Description": [],
            "VarRead": True,
            "VarWrite": False,
            "LongHelp": "",
            "ShortHelp": "The ID name of the node",
            "Name": "ID",
            "SeeAlso": [],
        },
    ],
}
