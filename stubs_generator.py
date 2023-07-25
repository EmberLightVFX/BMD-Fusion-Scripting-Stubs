"""
Convert json generated files to python stubs

TODO:
*   If a method has two usage with the same inputs but different outputs,
    combine them and make multiple output types instead
*   If the method is a constructor (eg ChannelStyle constructor),
    figure out what to do with it
*   GLView for some reason imports:
        from , import _,
        from  import _
*   Media_pool_item's class name contain spaces
*   MtlGraph3D imports "from Request req import _Request req"
*   Make sure Opertator.pyi doesn't import None from _None
*   RefObject.pyi uses "void", what should void be?
*   Request.pyi imports TimeStamp, waht should it be?

"""

import json
from pathlib import Path
import re


return_types: list[str] = []
add_overload = False
add_any = False


def typeConverter(type_string: str, is_optional=False) -> str:
    return_string = ""
    match type_string:
        case "boolean":
            return_string = "bool"
        case "number":
            return_string = "int"
        case "number (integer)":
            return_string = "int"
        case "integer":
            return_string = "int"
        case "int":
            return_string = "int"
        case "int8":
            return_string = "int"
        case "uint8":
            return_string = "int"
        case "int16":
            return_string = "int"
        case "uint16":
            return_string = "int"
        case "int32":
            return_string = "int"
        case "uint32":
            return_string = "int"
        case "int64":
            return_string = "int"
        case "uint64":
            return_string = "int"
        case "size_t":
            return_string = "int"
        case "float32":
            return_string = "float"
        case "float64":
            return_string = "float"
        case "value":
            return_string = "int"
        case "string":
            return_string = "str"
        case "char":
            return_string = "str"
        case "char8":
            return_string = "str"
        case "char16":
            return_string = "str"
        case "char32":
            return_string = "str"
        case "char64":
            return_string = "str"
        case "table":
            global add_any
            add_any = True
            return_string = "dict[Any, Any]"
        case "nil":
            return_string = "None"
        case _:
            return_string = f"_{type_string}"
            global return_types
            if type_string not in return_types:
                return_types.append(type_string)
    if is_optional:
        return_string += f" = {return_string}()"
    return return_string


def genTypeList(types: list[str] | str, is_optional=False):
    if isinstance(types, str):
        types = types.split("|")
    for i in range(len(types)):
        types[i] = typeConverter(types[i], is_optional)
    return " | ".join(types) if len(types) > 1 else "".join(types)


def genInputType(txt: str, is_optional=False):
    # Split at the first space only
    txt_list = txt.split(" ", 1)
    if len(txt_list) == 1:
        return txt_list[0].replace("-", "_").replace(" ", "_")
    return f"{txt_list[1].replace('-', '_').replace(' ', '_')}: {genTypeList(txt_list[0], is_optional)}"


def genStubs(o) -> tuple[str, list[str]]:
    print("Name: ", o["name"])
    content = f'class _{o["name"]}:\n'
    global return_types
    global add_overload
    global add_any
    add_overload = False
    add_any = False
    return_types = []

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
                content += f': {typeConverter(key["return_type"])}'
            else:
                content += f": Any"
                add_any = True
            content += "\n"

            if (
                key.get("short_help")
                or key.get("description")
                or key.get("access_class")
            ):
                content += f'\t"""\n'
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

    if o.get("attributes") and len(o["attributes"]) > 0:
        content += "\n\t#---Attributes---#\n"
        for name, key in o["attributes"].items():
            content += f"\t{name}"

            if key.get("value"):
                content += f': {typeConverter(key["value"])}\n'

            content += "\n"

    if o.get("methods") and len(o["methods"]) > 0:
        content += "\n\t#---Methods---#\n"
        for name, key in o["methods"].items():
            # Check if the item is something to process (if it's a dict or just a string)
            do_process = len(key) > 0 and isinstance(key, dict)

            # Fetch the help-string
            short_help = ""
            if do_process and (key.get("short_help") or key.get("description")):
                short_help += f'\t\t"""\n'
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

            if do_process and key.get("usage"):
                pattern = r"\((?:[^()]*|\((?:[^()]*|\([^()]*\))*\))*\)"

                is_overload = len(key["usage"]) > 1
                if is_overload:
                    add_overload = True
                for usage in key["usage"]:
                    if is_overload:
                        content += "\t@overload\n"
                    content += f"\tdef {name}(self"
                    splits = usage.split(" :")

                    # Process the input types
                    if len(splits) > 1:
                        if matches := re.findall(pattern, splits[1]):
                            # If the match is just an empty (), continue
                            if matches[0] != "()":
                                content += ", "
                                matches = matches[0].split(", ")
                                for i, match in enumerate(matches):
                                    match = match.replace("(", "").replace(")", "")
                                    if i > 0:
                                        content += ", "
                                    is_optional = False
                                    if match[0] == "[":
                                        is_optional = True
                                        match = match.replace("[", "").replace("]", "")
                                    content += genInputType(match, is_optional)

                    content += ")"

                    # # Get all return types
                    usage_types = splits[0].strip().replace("(", "").replace(")", "")
                    usage_splits = usage_types.split(", ")
                    content += " -> "
                    if usage_splits[0] != "":
                        if len(usage_splits) > 1:
                            content += "tuple["
                        for i, splits in enumerate(usage_splits):
                            if i > 0:
                                content += ", "
                            multi_splits = splits.split("|")
                            content += genTypeList(multi_splits)
                        if len(usage_splits) > 1:
                            content += "]"
                    else:
                        content += "None"
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
    typings_folder = root_folder / "typings"
    for file_path in json_stubs_folder.iterdir():
        if file_path.is_file():
            # Read the Markdown content from the file or fetch it from a URL.
            object_data = None

            with open(file_path, "r") as f:
                object_data = json.load(f)

            stubs_content, imports_to_add = genStubs(object_data)

            imports = "from typing import" if add_any or add_overload else ""
            if add_any:
                imports += " Any"
            if add_overload:
                imports += ", overload"
            if add_any or add_overload:
                imports += "\n\n"

            if len(imports_to_add) > 0:
                for imp in imports_to_add:
                    imports += f"from {imp} import _{imp}\n"
                imports += "\n\n"

            stubs_content = imports + stubs_content
            stubs_content += f'\n{object_data["name"]} = _{object_data["name"]}'
            stub_names.append(object_data["name"])

            # Save the stubs to a .pyi file
            with open(
                f"{typings_folder / file_path.stem}.pyi", "w", encoding="utf-8"
            ) as f:
                f.write(stubs_content)

        butilins_content = "".join(
            f"from {name} import {name}\n" for name in stub_names
        )
        butilins_content += "\n__all__ = ["
        for name in stub_names:
            butilins_content += f'\n\t"{name}",'
        butilins_content += "\n]"

        with open(f'{typings_folder / "__builtins__.pyi"}', "w", encoding="utf-8") as f:
            f.write(butilins_content)
