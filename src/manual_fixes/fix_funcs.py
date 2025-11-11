from dataclasses import dataclass
from .method_inputs import method_inputs_to_fix
from .method_return import method_return_types_to_fix
from .property_return import property_return_types_to_fix
from .argument_names import argument_names_to_fix
from .optional import optional_to_fix


@dataclass
class FixTypes:
    type: str
    extra_import: set[str] | None = None


def fix_optional(
    class_name: str, obj_name: str, input_name: str, old_optional: bool
) -> bool:
    if get_class := optional_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            if get_obj["input_name"] == input_name:
                if not isinstance(get_obj["optional"], bool):
                    assert False, "optional must be a bool"
                return get_obj["optional"]
    return old_optional


def fix_argument_names(
    class_name: str,
    obj_name: str,
    input_name: str,
) -> FixTypes:
    if get_class := argument_names_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            if get_obj["old_arg_name"] == input_name:
                return FixTypes(
                    get_obj["new_arg_name"],  # type: ignore
                )
    return FixTypes(input_name)


def fix_method_input_types(
    class_name: str,
    obj_name: str,
    input_name: str,
    old_input_type: str,
) -> FixTypes:
    if get_class := method_inputs_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            if (
                get_obj["input_name"] == input_name
                and get_obj["old_input_type"] == old_input_type
            ):
                # Check if extra_import is a list or a string
                if isinstance(get_obj["extra_import"], list):
                    extra_import_set = set(get_obj["extra_import"])
                elif isinstance(get_obj["extra_import"], str):
                    extra_import_set = set([get_obj["extra_import"]])
                else:
                    extra_import_set = None

                return FixTypes(
                    get_obj["input_type"],  # type: ignore
                    extra_import_set,
                )
    return FixTypes(old_input_type)


def fix_method_return_types(
    class_name: str,
    obj_name: str,
    old_return_type: str,
) -> FixTypes:
    if get_class := method_return_types_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            if get_obj["old_return_type"] == old_return_type:
                # Check if extra_import is a list or a string
                if isinstance(get_obj["extra_import"], list):
                    extra_import_set = set(get_obj["extra_import"])
                elif isinstance(get_obj["extra_import"], str):
                    extra_import_set = set([get_obj["extra_import"]])
                else:
                    extra_import_set = None

                return FixTypes(
                    get_obj["return_type"],  # type: ignore
                    extra_import_set,
                )
    return FixTypes(old_return_type)


def fix_property_return_types(
    class_name: str,
    property_name: str,
    old_return_type: str,
) -> FixTypes:
    if get_class := property_return_types_to_fix.get(class_name):
        if get_obj := get_class.get(property_name):
            # Check if extra_import is a list or a string
            if isinstance(get_obj["extra_import"], list):
                extra_import_set = set(get_obj["extra_import"])
            elif isinstance(get_obj["extra_import"], str):
                extra_import_set = set([get_obj["extra_import"]])
            else:
                extra_import_set = None

            return FixTypes(
                get_obj["return_type"],  # type: ignore
                extra_import_set,
            )
    return FixTypes(old_return_type)
