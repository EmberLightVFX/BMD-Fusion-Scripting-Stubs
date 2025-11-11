"""

!TODO:

TODO:
* Image.pyi imports Any even tho it's not used. This happens because a fix removed the Any from the objects

"""

import os
import subprocess
from pathlib import Path
import json
from typing import Any
from converters.string_converter import replace_with_underscore
from generators.stub_generator import generate_stubs, generate_non_existing_classes
from manual_fixes.generate_default_files import (
    generate_tool_class,
    generate_tool_scripts,
    generate_builtins,
)


def format_code_in_folder_with_ruff(folder_path: str):
    try:
        # Run the ruff command to format the file
        subprocess.run(
            ["ruff", "check", "--select=F401", "--fix", folder_path], check=True
        )
        print(f"Formatted {folder_path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while formatting {folder_path}: {e}")


def cleanup_methods(
    methods_data: list[dict[str, Any]],
) -> dict[str, dict[str, str]]:
    flattened_methods = {}
    for method_group in methods_data:
        for item in method_group["items"]:
            flattened_methods[item["name"]] = {
                "usage": item["usage"],
                "short_help": item["short_help"],
                "description": item["description"],
            }
    return flattened_methods


def cleanup_properties(
    properties_data: list[dict[str, Any]],
) -> dict[str, dict[str, str]]:
    flattened_properties = {}
    for prop_group in properties_data:
        for item in prop_group["items"]:
            flattened_properties[item["name"]] = {
                "return_type": item["return_type"]
                .replace("Type: ", "")
                .replace("Types: ", ""),
                "short_help": item["short_help"],
                "description": item["description"],
                "access_class": item.get("access_class", ""),
            }
    return flattened_properties


def main():
    root_folder = Path(__file__).parent.parent
    json_stubs_file = root_folder / "Fusion_fusion_stubs.json"
    typings_folder = root_folder / "fusion-stubs"

    with open(json_stubs_file, "r", encoding="utf-8", errors="replace") as f:
        fusion_stubs = json.load(f)

    generated_types = ["Tool"]

    # Process data once and store results
    for object_data in fusion_stubs:
        generated_types.append(replace_with_underscore(object_data["Name"]))

    # Use processed data for stub generation
    for object_data in fusion_stubs:
        # if object_data["Name"] != "Operator":
        #    continue
        stubs_content = generate_stubs(
            object_data,
            generated_types,
        )

        name_with_underscores = replace_with_underscore(object_data["Name"])
        if not os.path.exists(typings_folder):
            os.mkdir(typings_folder)

        with open(
            typings_folder / f"{name_with_underscores}.pyi", "w", encoding="utf-8"
        ) as f:
            f.write(stubs_content)

    # Generate additional files
    with open(
        os.path.join(typings_folder, "_non_existing.pyi"), "w", encoding="utf-8"
    ) as f:
        f.write(generate_non_existing_classes())

    with open(typings_folder / "Tool.pyi", "w", encoding="utf-8") as f:
        f.write(generate_tool_class())

    with open(typings_folder / "_tool_scripts.pyi", "w", encoding="utf-8") as f:
        f.write(generate_tool_scripts())

    with open(typings_folder / "__builtins__.pyi", "w", encoding="utf-8") as f:
        f.write(generate_builtins())
        for object_name in generated_types:
            f.write(f"from .{object_name} import {object_name}\n")
        f.write("\n__all__.extend([\n")
        for object_name in generated_types:
            f.write(f'    "{object_name}",\n')
        f.write("])\n")

    format_code_in_folder_with_ruff(typings_folder.as_posix())


if __name__ == "__main__":
    main()
