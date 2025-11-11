from typing import Any
from dataclasses import dataclass
from converters.type_converter import type_converter
from manual_fixes import (
    fix_property_return_types,
    additional_properties_list,
)
from converters.string_converter import fix_type_name, format_docstring


@dataclass
class PropertyGeneratorResult:
    content: str
    requires_any: bool = False
    extra_imports: set[str] | None = None


def gen_properties(
    obj_data: dict[str, Any],
) -> PropertyGeneratorResult:
    if additional_properties_list.get(obj_data["Name"]):
        obj_data["Properties"].extend(additional_properties_list[obj_data["Name"]])

    content = "\n    #---Properties---#\n"
    requires_any = False
    extra_imports = set()
    for property in obj_data["Properties"]:
        # If property is not accessible, skip it
        if property["VarRead"] is False and property["VarWrite"] is False:
            continue
        content += f"    {property['Name']}"

        if not property["Usage"]:
            content += ": Any\n\n"
            requires_any = True
            continue

        if len(property["Usage"]) > 2:
            print(property)
            raise Exception("Multiple usages found!!!!!")

        if property["Usage"][0]["Returns"]:
            return_name = type_converter(
                fix_type_name(property["Usage"][0]["Returns"][0]["Type"]),
                obj_data["Name"],
            )

            fix = fix_property_return_types(
                obj_data.get("Name", ""),
                property.get("Name", ""),
                return_name.return_string,
            )

            content += f": {fix.type}"
            if return_name.custom_return:
                extra_imports.add(return_name.custom_return)
            requires_any = requires_any or return_name.requires_any
        else:
            content += ": Any"
            requires_any = True
        content += "\n"

        has_description = False
        for description in property["Description"]:
            if description["Text"] != "":
                has_description = True
        if (
            property["ShortHelp"] != ""
            or has_description
            or (property["VarRead"] is True and property["VarWrite"] is False)
            or (property["VarRead"] is False and property["VarWrite"] is True)
        ):
            content += generate_property_docstring(property)
            content += "\n"

        content += "\n"
    return PropertyGeneratorResult(content, requires_any, extra_imports)


def generate_property_docstring(property: dict[str, Any]) -> str:
    """Generate property docstring from help text"""
    docstring = '    """\n'

    if property["ShortHelp"] != "":
        docstring += f"{format_docstring(property['ShortHelp'], '    ')}\n\n"

    for description in property["Description"]:
        if description["Text"] != "":
            docstring += f"{format_docstring(description['Text'], '    ')}\n\n"

    if property.get("VarRead") is True and property.get("VarWrite") is False:
        docstring += "    Read Only\n"
    elif property.get("VarRead") is False and property.get("VarWrite") is True:
        docstring += "    Write Only\n"

    docstring = docstring[:-1]
    docstring += '\n    """'

    return docstring
