from dataclasses import dataclass
from typing import Any
from generators.property_generator import gen_properties
from generators.registry_generator import gen_registry
from generators.method_generator import gen_methods
from converters.string_converter import replace_with_underscore

non_existing_imports = set()


@dataclass
class StubGeneratorResult:
    content: str
    imports: str


def generate_stubs(
    obj_data: dict[str, Any],
    generated_types: list[str],
) -> str:
    imports_list = set()
    content = f"class {replace_with_underscore(obj_data['Name'])}:\n"

    # Check if object is empty
    if (
        not obj_data.get("Properties")
        and not obj_data.get("Registry")
        and not obj_data.get("Methods")
    ):
        content += "    ...\n"
        return content

    # Generate properties
    if obj_data.get("Properties") and len(obj_data["Properties"]) > 0:
        prop_result = gen_properties(obj_data)
        content += prop_result.content
        if prop_result.requires_any:
            imports_list.add("Any")
        if prop_result.extra_imports:
            imports_list.update(prop_result.extra_imports)

    # Generate registry
    if obj_data.get("Registry") and len(obj_data["Registry"]) > 0:
        reg_result = gen_registry(obj_data)
        content += reg_result.content
        if reg_result.extra_imports:
            imports_list.update(reg_result.extra_imports)

    # Generate methods
    if obj_data.get("Methods") and len(obj_data["Methods"]) > 0:
        method_result = gen_methods(obj_data)
        content += method_result.content
        if method_result.requires_overload:
            imports_list.add("overload")
        if method_result.requires_any:
            imports_list.add("Any")
        if method_result.requires_literal:
            imports_list.add("Literal")
        if method_result.extra_imports:
            imports_list.update(method_result.extra_imports)

    # Generate imports
    imports = generate_imports(imports_list, generated_types)

    return imports + content


def generate_imports(imports_list: set[str], generated_types: list[str]) -> str:
    typing_imports = []
    type_imports = []
    local_non_existing_imports = []

    for imp in imports_list:
        if imp in ["Any", "overload", "Literal"]:
            typing_imports.append(imp)
        elif imp in generated_types:
            type_imports.append(imp)
        elif imp not in [
            "str",
            "int",
            "float",
            "bool",
            "list",
            "dict",
            "tuple",
            "set",
            "bytes",
            "bytearray",
            "complex",
            "range",
            "slice",
            "object",
            "type",
            None,
        ]:
            local_non_existing_imports.append(imp)

    imports = ""
    if typing_imports:
        imports += f"from typing import {', '.join(typing_imports)}\n\n"

    for imp in type_imports:
        imports += f"from {imp} import {imp}\n"

    if local_non_existing_imports:
        imports += (
            f"from _non_existing import {', '.join(local_non_existing_imports)}\n"
        )
        non_existing_imports.update(set(local_non_existing_imports))

    if len(type_imports) > 0 or len(local_non_existing_imports) > 0:
        imports += "\n\n"

    return imports


def generate_non_existing_classes() -> str:
    """Generate stub classes for non-existing types"""
    content = ""
    for obj in non_existing_imports:
        content += f"class {obj}:\n    ...\n\n"
    return content
