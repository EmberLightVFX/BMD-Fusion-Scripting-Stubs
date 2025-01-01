def remove_parentheses(string: str) -> str:
    return string.replace("(", "").replace(")", "").strip()


def remove_brackets(string: str) -> str:
    return string.replace("[", "").replace("]", "").strip()


def remove_colon(string: str) -> str:
    return string.replace(":", "").strip()


def replace_dots_from_name(string: str) -> str:
    return string.replace(".", "_").strip()


def replace_with_underscore(string: str) -> str:
    return string.replace("-", "_").replace(" ", "_")


def fix_illegal_names(string: str) -> str:
    if string in {"def", "from"}:
        string = f"{string}_"
    return string


def fix_multi_input_names(string: str) -> str:
    return string.replace("|", "_or_")


def fix_prob_chars(string: str) -> str:
    """Remove characters that shouldn't be there from the Fusion Docs"""
    return (
        string.replace("ï¿½@ï¿½vIhï¿½%<ï¿½", "")
        .replace("ð@‚vIhÂ%<½", "")
        .replace("�@�vIh�%<�", "")
        .replace("@vIh%<", "")
        .replace("�������?�������?�������?�������?", "")
        .replace("�@", "")
        .replace("����������������", "")
    )


def fix_type_name(name: str) -> str:
    return fix_prob_chars(
        fix_multi_input_names(
            fix_illegal_names(
                replace_dots_from_name(
                    replace_with_underscore(
                        name,
                    )
                )
            )
        )
    )


def format_docstring(string: str, tabs: str = "") -> str:
    new_str = []
    lines = string.strip().split("\n")
    for line in lines:
        new_str.append(f"{tabs}{line.strip()}")

    return "\n".join(new_str)
