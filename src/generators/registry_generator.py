from dataclasses import dataclass
from typing import Any
from converters.type_converter import type_converter


@dataclass
class RegistryGeneratorResult:
    content: str
    extra_imports: list[str] | None = None


def gen_registry(obj_data: dict[str, Any]) -> RegistryGeneratorResult:
    content = "\n    #---Registry---#\n"
    extra_imports = []

    for object in obj_data["Registry"]:
        content += f"    {object['FullName']}"
        if object.get("Value"):
            result = type_converter(object["Value"], obj_data["Name"])
            content += f": {result.return_string}\n"
            if result.custom_return:
                extra_imports.append(result.custom_return)
        content += "\n"

    return RegistryGeneratorResult(content, extra_imports)
