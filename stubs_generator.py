"""
Convert json generated files to python stubs

Fixed:
*   If a method has two usage with the same inputs but different outputs,
    combine them and make multiple output types instead
*   If the method is a constructor (eg ChannelStyle constructor),
    figure out what to do with it
*   GLView for some reason imports:
        from , import _,
        from  import _
*   Media_pool_item's class name contain spaces
*   MtlGraph3D imports "from Request req import _Request req"
*   Fetch all return types that aren't native but also not objects

TODO:
*   How to deal with:
    "info_text":    "Discovered methods might be available in many contexts,
                    but most typically in Fuse scripts",

"""

import json
from pathlib import Path
import re


return_types: list[str] = []
non_existing_types: list[str] = []
local_non_existing_types: list[str] = []
json_files: list[str] = []
add_overload = False
add_any = False
add_literal = False


def removeParents(string: str) -> str:
    return string.replace("(", "").replace(")", "").strip()


def removeBrackets(string: str) -> str:
    return string.replace("[", "").replace("]", "").strip()


def removeColon(string: str) -> str:
    return string.replace(":", "").strip()


def replaceDotsFromName(string: str) -> str:
    return string.replace(".", "_").strip()


def replaceWithUnderscore(string: str):
    return string.replace("-", "_").replace(" ", "_")


def fixProbChars(string: str):
    """Remove characters that shouldn't be there from the Fusion Docs"""
    return (
        string.replace("ï¿½@ï¿½vIhï¿½%<ï¿½", "")
        .replace("ð@‚vIhÂ%<½", "")
        .replace("�@�vIh�%<�", "")
        .replace("@vIh%<", "")
    )


def fixIllegalNames(string: str) -> str:
    if string in {
        "def",
        "from",
    }:
        string = f"{string}_"
    return string


def fixMultiInputNames(string: str) -> str:
    return string.replace("|", "_or_")


def generateNonExistingClasses(non_existing_types: list[str]) -> str:
    content = "".join(f"class {obj}_:\n\t...\n" for obj in non_existing_types) + "\n"
    for obj in non_existing_types:
        content += f"{obj} = {obj}_\n"
    content += "\n"
    return content


def generateToolClass() -> str:
    return """\
from Operator import Operator_

Tool_ = Operator_

"""


def generateToolScripts() -> str:
    return """\
from Fusion import Fusion_
from Composition import Composition_
from Tool import Tool_

fusion = Fusion_()
fu = Fusion_()

composition = Composition_()
comp = Composition_()

tool = Tool_()

"""


def generateBuiltins() -> str:
    return """\
from _tool_scripts import fusion, fu, composition, comp, tool

__all__ = [
    "fusion",
    "fu",
    "composition",
    "comp",
    "tool"
]
"""


def typeConverter(type_string: str, is_optional=False, name: str = "") -> str:
    return_string = ""

    if type_string == "boolean":
        return_string = "bool"
    elif type_string in {
        "number",
        "number (integer)",
        "integer",
        "int",
        "int8",
        "uint8",
        "int16",
        "uint16",
        "int32",
        "uint32",
        "int64",
        "uint64",
        "size_t",
    }:
        return_string = "int"
    elif type_string in {
        "value",
        "float32",
        "float64",
    }:
        return_string = "float"
    elif type_string in {
        "string",
        "char",
        "char_t",
        "char8",
        "char8_t",
        "char16",
        "char16_t",
        "char32",
        "char32_t",
        "char64",
        "char64_t",
    }:
        return_string = "str"
    elif type_string == "table":
        global add_any
        add_any = True
        return_string = "dict[Any, Any]"
    elif type_string == "nil":
        return_string = "None"
    else:
        return_string = f"{type_string}_"
        global return_types
        if type_string != name and type_string not in return_types:
            return_types.append(type_string)
            if type_string != "Tool":
                global json_files
                global non_existing_types
                global local_non_existing_types
                if f"{type_string}.json" not in json_files:
                    local_non_existing_types.append(type_string)
                    if type_string not in non_existing_types:
                        non_existing_types.append(type_string)

    if is_optional:
        return_string += f" = {return_string}()"
    return return_string


def genTypeList(types: list[str] | str, is_optional=False, name=""):
    if isinstance(types, str):
        types = types.split("|")
    for i in range(len(types)):
        types[i] = typeConverter(types[i], is_optional, name)
    return " | ".join(types) if len(types) > 1 else "".join(types)


def genInputType(txt: str, is_optional=False, name=""):
    # Split at the first space only
    txt_list = txt.split(" ", 1)
    if len(txt_list) == 1:
        return fixMultiInputNames(fixIllegalNames(replaceWithUnderscore(txt_list[0])))
    new_name = fixMultiInputNames(fixIllegalNames(replaceWithUnderscore(txt_list[1])))
    if "§" in new_name:
        global add_literal
        add_literal = True
        literals = new_name.split("§")
        rest_literals = ", ".join(f'"{literal}"' for literal in literals[1:])
        return f"{literals[0]}: Literal[{rest_literals}]"
    return f"{new_name}: {genTypeList(txt_list[0], is_optional, name)}"


def genStubs(o) -> tuple[str, list[str]]:
    print("Name: ", o["name"])
    content = f'class {replaceWithUnderscore(o["name"])}_:\n'
    global return_types
    global add_overload
    global add_any
    global local_non_existing_types
    global add_literal
    add_overload = False
    add_any = False
    return_types = []
    local_non_existing_types = []
    add_literal = False

    # Check if object is empty:
    if not o.get("properties") and not o.get("attributes") and not o.get("methods"):
        content += "\t...\n"
        return content, return_types

    ## PROPERTIES ##
    if o.get("properties") and len(o["properties"]) > 0:
        content += "\n\t#---Properties---#\n"
        for name, key in o["properties"].items():
            if isinstance(key, str):
                continue

            content += f"\t{name}"
            # If key is list, meaning no real information inside:
            if isinstance(key, list):
                content += ": Any\n"
                add_any = True
                continue

            if key.get("return_type"):
                content += f': {typeConverter(key["return_type"], name=o["name"])}'
            else:
                content += ": Any"
                add_any = True
            content += "\n"

            if (
                key.get("short_help")
                or key.get("description")
                or key.get("access_class")
            ):
                content += '\t"""\n'
                if key.get("short_help"):
                    content += f'\t{key["short_help"]}\n\n'
                if key.get("description"):
                    # Split the string into lines
                    lines = key["description"].split("\n")
                    # Add two tabs (8 spaces) to each line except the first one
                    indented_lines = [
                        "\t\t" + line if line.strip() else line for line in lines
                    ]
                    # Convert any two spaces to four spaces
                    converted_lines = [
                        line.replace("  ", "\t") for line in indented_lines
                    ]
                    # Join the lines back together
                    output_string = "\n".join(converted_lines)
                    content += f"\t{output_string}\n\n"
                if key.get("access_class"):
                    content += f'\t{key["access_class"]}\n'

                # As we don't know if short_help and description exist well
                # delete the two last characters in the string here to make sure
                # we end up on one single new line
                content = content[:-1]
                content += '\n\t"""'

            content += "\n"

    ## ATTRIBUTES ##
    if o.get("attributes") and len(o["attributes"]) > 0:
        content += "\n\t#---Attributes---#\n"
        for name, key in o["attributes"].items():
            content += f"\t{name}"

            if key.get("value"):
                content += f': {typeConverter(key["value"], name=o["name"])}\n'

            content += "\n"

    ## METHODS ##
    if o.get("methods") and len(o["methods"]) > 0:
        # Pattern to catch everything within ()
        input_type_pattern = r"\((?:[^()]*|\((?:[^()]*|\([^()]*\))*\))*\)"
        # Define the regular expression pattern
        return_type_pattern = r"\|(?![^(]*\))"
        """
        Pre Process the methods to look for duplicate objects
        with same input variables. If found, combine them into one
        """
        for name, key in o["methods"].items():
            do_process = len(key) > 0 and isinstance(key, dict)
            if do_process and key.get("usage") and len(key["usage"]) > 1:
                new_usage: list[str] = []
                for usage in key["usage"]:
                    splits = usage.split(" :")
                    # Process the input types
                    if len(splits) > 1:
                        new_nu = True
                        for i, nu in enumerate(new_usage):
                            nu_splits = nu.split(" :")
                            if len(nu_splits) > 1 and splits[1] == nu_splits[1]:
                                new_nu = False
                                new_usage[
                                    i
                                ] = f"({splits[0]}|{nu_splits[0]}) :{splits[1]}"
                                break
                        if new_nu:
                            new_usage.append(f"{splits[0]} :{splits[1]}")
                key["usage"] = new_usage

        content += "\n\t#---Methods---#\n"
        for name, key in o["methods"].items():
            # Check if the item is something to process (only process dicts)
            do_process = len(key) > 0 and isinstance(key, dict)

            # Fetch the help-string
            short_help = ""
            if do_process and (key.get("short_help") or key.get("description")):
                short_help += '\t\t"""\n'
                if key.get("short_help"):
                    short_help += f'\t\t{key["short_help"]}\n\n'
                if key.get("description"):
                    # Split the string into lines
                    lines = key["description"].split("\n")
                    # Add two tabs (8 spaces) to each line except the first one
                    indented_lines = [
                        "\t\t" + line if line.strip() else line for line in lines
                    ]
                    # Convert any two spaces to four spaces
                    converted_lines = [
                        line.replace("  ", "\t") for line in indented_lines
                    ]
                    # Join the lines back together
                    output_string = "\n".join(converted_lines)
                    short_help += f"{output_string}\n\n"

                # As we don't know if short_help and description exist well
                # delete the two last characters in the string here to make sure
                # we end up on one single new line
                short_help = short_help[:-1]
                short_help += '\t\t"""\n'
            short_help += "\t\t...\n"

            # Process all usage types
            if do_process and key.get("usage"):
                if is_overload := len(key["usage"]) > 1:
                    add_overload = True
                for usage in key["usage"]:
                    if is_overload:
                        content += "\t@overload\n"
                    content += f"\tdef {name}(self"

                    # Split the input and return types
                    splits = usage.split(f"{name}(")

                    # Process the input types
                    if len(splits) > 1:
                        if matches := re.findall(input_type_pattern, f"({splits[1]}"):
                            # If the match is just an empty (), continue
                            if matches[0] != "()":
                                content += ", "
                                matches = replaceDotsFromName(matches[0]).split(", ")

                                # Check if string is of type Literal
                                # If litterlas are found, tag them with §
                                filtered_matches = []
                                is_literal = False
                                for match in matches:
                                    if ":" in match and is_literal is False:
                                        is_literal = True
                                        match_split = match.split(": ")
                                        filtered_matches.append(
                                            f"{match_split[0]}§{match_split[1]}"
                                        )
                                    elif is_literal is True:
                                        if " " in match:  # No longer literals
                                            is_literal = False
                                            filtered_matches.append(match)
                                        else:  # Literals - Add § between each object
                                            filtered_matches[-1] += f"§{match}"
                                    else:
                                        filtered_matches.append(match)

                                # Go through all matches and extract input types
                                for i, match in enumerate(filtered_matches):
                                    match = removeParents(match)
                                    if i > 0:
                                        content += ", "
                                    is_optional = False
                                    if match[0] == "[":
                                        is_optional = True
                                        match = removeBrackets(match)
                                    content += genInputType(
                                        match, is_optional, name=o["name"]
                                    )

                    # process all return types
                    content += ") -> "
                    splits[0] = removeColon(fixProbChars(splits[0]))
                    return_type_result = re.split(return_type_pattern, splits[0])
                    for r_i, r_splits in enumerate(return_type_result):
                        if r_i > 0:
                            content += " | "
                        usage_types = removeParents(r_splits)
                        usage_splits = usage_types.split(", ")
                        if usage_splits[0] == "":
                            content += "None"
                        else:
                            # Catch errors in the fusion docs:
                            # If the return type is an empty whitespace
                            # remove it from the list
                            for i, splits in enumerate(usage_splits):
                                if splits == ",":
                                    del usage_splits[i]

                            # Check if it's a constructor:
                            construct_split = usage_splits[0].split(" ")
                            if len(construct_split) > 1 and removeParents(
                                construct_split[0]
                            ) == removeParents(construct_split[1]):
                                content += f"{removeParents(construct_split[0])}_"

                            else:  # Normal return type
                                if len(usage_splits) > 1:
                                    content += "tuple["
                                for i, splits in enumerate(usage_splits):
                                    if i > 0:
                                        content += ", "
                                    multi_splits = splits.split("|")
                                    content += genTypeList(multi_splits, name=o["name"])
                                if len(usage_splits) > 1:
                                    content += "]"
                    content += ":\n"
                    content += short_help
            else:
                content += f"\tdef {name}(self):\n{short_help}"

    return content, return_types


if __name__ == "__main__":
    stub_names: list[str] = []
    object_data = None

    # Loop through all files inside the json_stubs folder
    root_folder = Path(__file__).parent
    json_stubs_folder = root_folder / "json_stubs"
    typings_folder = root_folder / "fusion_typings"

    # Get a list of all filenames available
    json_files = [
        file.name
        for file in json_stubs_folder.iterdir()
        if file.is_file() and file.suffix == ".json"
    ]
    ## Process all json files ##
    for file_path in json_stubs_folder.iterdir():
        if file_path.is_file() and file_path.suffix == ".json":
            # Read the Markdown content from the file or fetch it from a URL.
            object_data = None
            with open(file_path, "r", encoding="utf-8") as f:
                object_data = json.load(f)

            stubs_content, imports_to_add = genStubs(object_data)

            imports_list = []
            if add_any:
                imports_list.append("Any")
            if add_overload:
                imports_list.append("overload")
            if add_literal:
                imports_list.append("Literal")

            imports = (
                "from typing import " + ", ".join(imports_list) + "\n\n"
                if imports_list
                else ""
            )

            if len(imports_to_add) > 0:
                for imp in imports_to_add:
                    if imp not in local_non_existing_types:
                        imports += f"from {imp} import {imp}_\n"
                if len(local_non_existing_types) > 0:
                    imports += "from _non_existing import "
                    for i, imp in enumerate(local_non_existing_types):
                        if i > 0:
                            imports += ", "
                        imports += f"{imp}_"
                    imports += "\n"
                imports += "\n\n"

            stubs_content = imports + stubs_content
            name_with_underscores = replaceWithUnderscore(object_data["name"])
            stubs_content += f"\n{name_with_underscores} = {name_with_underscores}_"
            stub_names.append(name_with_underscores)

            # Save the stubs to a .pyi file
            with open(
                f"{typings_folder / file_path.stem}.pyi", "w", encoding="utf-8"
            ) as f:
                f.write(stubs_content)

    ## Write non-existing objects to file ##
    with open(f'{typings_folder / "_non_existing.pyi"}', "w", encoding="utf-8") as f:
        f.write(generateNonExistingClasses(non_existing_types))

    ## Write tool class ##
    with open(f'{typings_folder / "Tool.pyi"}', "w", encoding="utf-8") as f:
        f.write(generateToolClass())

    ## Write tool scripts ##
    with open(f'{typings_folder / "_tool_scripts.pyi"}', "w", encoding="utf-8") as f:
        f.write(generateToolScripts())

    ## Generate __builtins__ files
    if True:
        with open(f'{typings_folder / "__builtins__.pyi"}', "w", encoding="utf-8") as f:
            f.write(generateBuiltins())
    else:  # For debugging
        butilins_content = (
            "".join(f"from {name} import {name}\n" for name in stub_names)
            + "\n__all__ = ["
        )
        for name in stub_names:
            butilins_content += f'\n\t"{name}",'
        butilins_content += "\n]"

        with open(f'{typings_folder / "__builtins__.pyi"}', "w", encoding="utf-8") as f:
            f.write(butilins_content)
