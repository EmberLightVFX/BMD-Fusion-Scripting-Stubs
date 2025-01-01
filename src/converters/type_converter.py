from dataclasses import dataclass


@dataclass
class TypeConversionResult:
    return_string: str
    custom_return: str = ""
    requires_any: bool = False


def type_converter(type_string: str, name: str = "") -> TypeConversionResult:
    return_string = ""
    custom_return = ""
    requires_any = False

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
    elif type_string in {"value", "float32", "float64"}:
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
        return_string = "dict[Any, Any]"
        requires_any = True
    elif type_string in {"nil", ""}:
        return_string = "None"
    elif "dict[" in type_string:
        return_string = type_string
    else:
        return_string = type_string
        if type_string != name:
            custom_return = type_string

    return TypeConversionResult(return_string, custom_return, requires_any)
