from typing import Optional


def add_extra_imports(
    extra_imports: str | list[str],
    generated_types: list[str],
    non_existing_types: list[str],
    local_non_existing_types: list[str],
    return_types: list[str],
) -> tuple[list[str], list[str], list[str]]:
    """Process and categorize imports"""
    if not isinstance(extra_imports, list):
        extra_imports = [extra_imports]

    for extra_import in extra_imports:
        # Remove trailing "_"
        extra_import = extra_import.replace("_", "")

        if extra_import not in generated_types:
            if extra_import not in local_non_existing_types:
                local_non_existing_types.append(extra_import)
            if extra_import not in non_existing_types:
                non_existing_types.append(extra_import)

        if extra_import and extra_import not in return_types:
            return_types.append(extra_import)

    return non_existing_types, local_non_existing_types, return_types


def add_return_type(
    return_type: str, extra_import: Optional[str], return_types: list[str]
) -> list[str]:
    """Add return type to the list of return types"""
    if extra_import and extra_import not in return_types:
        return_types.append(extra_import)
    return return_types
