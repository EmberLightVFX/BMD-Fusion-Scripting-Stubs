from dataclasses import dataclass
from typing import Any
from converters.type_converter import (
    TypeConversionResult,
    type_converter,
)
from converters.string_converter import (
    remove_parentheses,
    fix_type_name,
    format_docstring,
)

from manual_fixes import (
    fix_method_return_types,
    fix_method_input_types,
    additional_methods_list,
    fix_argument_names,
    fix_optional,
)


@dataclass
class MethodGeneratorResult:
    content: str
    requires_overload: bool = False
    requires_any: bool = False
    requires_literal: bool = False
    extra_imports: set[str] | None = None


def gen_methods(obj_data: dict[str, Any]) -> MethodGeneratorResult:
    if additional_methods_list.get(obj_data["Name"]):
        obj_data["Methods"].extend(additional_methods_list[obj_data["Name"]])

    # TODO: I think this function isn't needed any longer?
    # obj_data = remove_duplicate_methods(obj_data)

    content = "\n\t#---Methods---#\n"
    requires_overload = False
    requires_any = False
    requires_literal = False
    extra_imports = set()

    for method in obj_data["Methods"]:
        print(obj_data["Name"], method["Name"])
        method_result = generate_method(obj_data, method)
        content += method_result.content
        requires_overload = requires_overload or method_result.requires_overload
        requires_any = requires_any or method_result.requires_any
        requires_literal = requires_literal or method_result.requires_literal
        if method_result.extra_imports:
            extra_imports.update(method_result.extra_imports)

    return MethodGeneratorResult(
        content, requires_overload, requires_any, requires_literal, extra_imports
    )


def remove_duplicate_methods(obj_data: dict[str, Any]) -> dict[str, Any]:
    for key in obj_data["methods"].keys():
        if (
            len(key) > 0
            and isinstance(key, dict)
            and key.get("usage")
            and len(key["usage"]) > 1
        ):
            new_usage: list[str] = []
            for usage in key["usage"]:
                splits = usage.split(" :")
                if len(splits) > 1:
                    new_nu = True
                    for i, nu in enumerate(new_usage):
                        nu_splits = nu.split(" :")
                        if len(nu_splits) > 1 and splits[1] == nu_splits[1]:
                            new_nu = False
                            new_usage[i] = f"({splits[0]}|{nu_splits[0]}) :{splits[1]}"
                            break
                    if new_nu:
                        new_usage.append(f"{splits[0]} :{splits[1]}")
            key["usage"] = new_usage
    return obj_data


def generate_method(
    obj: dict[str, Any],
    method: dict[str, Any],
) -> MethodGeneratorResult:
    requires_overload = False
    requires_any = False
    requires_literal = False
    extra_imports = set()

    content = ""

    do_docstring = (
        True
        if method.get("ShortHelp")
        or (method.get("Description") and method["Description"][0].get("Text") != "")
        else False
    )

    if method["Usage"]:
        is_overload = len(method["Usage"]) > 1
        requires_overload = is_overload

        for usage in method["Usage"]:
            if is_overload:
                content += "\t@overload\n"
            content += f'\tdef {method["Name"]}(self'

            method_signature = generate_method_signature(obj, method, usage)
            requires_any = requires_any or method_signature.requires_any
            requires_literal = requires_literal or method_signature.requires_literal
            if method_signature.extra_imports:
                extra_imports.update(method_signature.extra_imports)

            content += method_signature.content + ":\n"
            if do_docstring:
                content += generate_method_docstring(obj, method, usage)

            content += "\t\t...\n\n"
    else:
        content = f'\tdef {method["Name"]}(self) -> None:\n'
        if do_docstring:
            content += generate_method_docstring(obj, method)
        content += "\t\t...\n\n"

    return MethodGeneratorResult(
        content,
        requires_overload,
        requires_any,
        requires_literal,
        extra_imports,
    )


# Additional helper functions would go here...


@dataclass
class MethodSignatureResult:
    content: str
    requires_any: bool = False
    requires_literal: bool = False
    extra_imports: set[str] | None = None


def generate_method_docstring(
    obj: dict[str, Any], method: dict[str, Any], usage: dict[str, Any] = {}
) -> str:
    """Generate method docstring from help text"""
    docstring = '\t\t"""\n'

    if method["ShortHelp"] != "":
        docstring += f'{format_docstring(method["ShortHelp"], "\t\t")}\n\n'

    if usage.get("Description") and usage["Description"] != "":
        docstring += f"{format_docstring(usage["Description"], "\t\t")}\n\n"

    for description in method["Description"]:
        if description["Text"] != "":
            docstring += f'{format_docstring(description["Text"], "\t\t")}\n\n'

    # Args
    args = []
    if usage:
        for arg in usage["Args"]:
            info = f"{arg['Name']} ("

            arg_type = fix_method_input_types(
                obj.get("Name", ""),
                method.get("Name", ""),
                arg.get("Name", ""),
                type_converter(fix_type_name(arg["Type"])).return_string,
            ).type

            if arg.get("Optional"):
                info += f"Optional[{arg_type}]"
            else:
                info += arg_type
            info += ")"
            if arg.get("Description"):
                info += f": {format_docstring(arg["Description"])}"
            args.append(info)

        if args:
            docstring += "\t\tArgs:\n"
            for arg in args:
                docstring += f"\t\t\t{arg}\n"
            docstring += "\n"

        # Returns
        returns = []
        for ret in usage["Returns"]:
            info = ""

            ret_type = ""
            if ret.get("Type"):
                ret_type = fix_method_return_types(
                    obj.get("Name", ""),
                    method.get("Name", ""),
                    type_converter(fix_type_name(ret["Type"])).return_string,
                ).type

            if ret.get("Name"):
                info += f"{ret['Name']}"
                if ret.get("Type"):
                    info += f" ({ret_type})"
            else:
                if ret.get("Type"):
                    info += f"{ret_type}"

            if ret.get("Description"):
                info += f": {format_docstring(ret['Description'])}"
            returns.append(info)

        if returns:
            docstring += "\t\tReturns:\n"
            for ret in returns:
                docstring += f"\t\t\t{ret}\n"
            docstring += "\n"

    docstring = docstring[:-1]
    docstring += '\t\t"""\n'

    return docstring


def generate_method_signature(
    obj: dict[str, Any], method: dict[str, Any], usage: dict[str, Any]
) -> MethodSignatureResult:
    """Generate method signature including input types and return type"""
    requires_any = False
    requires_literal = False
    extra_imports = set()

    content = ""

    for arg in usage["Args"]:
        types = fix_method_types(arg["Type"], obj["Name"])
        corrected_types = []
        for type in types:
            corrected_types.append(type.return_string)
            if type.custom_return:
                extra_imports.add(type.custom_return)
            requires_any = requires_any or type.requires_any
        fixed_arg_name = fix_argument_names(
            obj["Name"],
            method["Name"],
            fix_type_name(
                arg["Name"],
            ),
        ).type
        fix = fix_method_input_types(
            obj.get("Name", ""),
            method.get("Name", ""),
            fixed_arg_name,
            " | ".join(corrected_types),
        )
        if fix.extra_import:
            extra_imports.update(fix.extra_import)
        content += f", {fixed_arg_name}: {fix.type}"
        if (
            arg.get("Optional")
            and fix_optional(
                obj.get("Name", ""),
                method.get("Name", ""),
                fixed_arg_name,
                arg["Optional"],
            )
            is True
        ):
            content += " | None = None"

    # Process return type
    content += ") -> "
    return_name = "None"
    if usage["Returns"]:
        corrected_return_types = []
        for arg in usage["Returns"]:
            types = fix_method_types(arg["Type"], obj["Name"])
            corrected_types = []
            for type in types:
                corrected_types.append(type.return_string)
                if type.custom_return:
                    extra_imports.add(type.custom_return)
                requires_any = requires_any or type.requires_any
            if len(corrected_types) > 1:
                corrected_return_types.append(f"({'|'.join(corrected_types)})")
            else:
                corrected_return_types.append(corrected_types[0])

        if len(corrected_return_types) > 1:
            return_name = f"({', '.join(corrected_return_types)})"
        else:
            return_name = corrected_return_types[0]
        fix = fix_method_return_types(
            obj.get("Name", ""),
            method.get("Name", ""),
            " | ".join(corrected_return_types),
        )
        return_name = fix.type
        if fix.extra_import:
            extra_imports.update(fix.extra_import)

    content += return_name

    return MethodSignatureResult(
        content,
        requires_any,
        requires_literal,
        extra_imports,
    )


def fix_method_types(types: str, name: str) -> list[TypeConversionResult]:
    corrected_types = []
    types = remove_parentheses(types)
    types_list = types.split("|")
    for type in types_list:
        corrected_types.append(type_converter(fix_type_name(type), name))
    return corrected_types
