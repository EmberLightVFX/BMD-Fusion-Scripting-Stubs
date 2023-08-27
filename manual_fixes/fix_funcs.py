from method_inputs import method_inputs_to_fix
from method_return import method_return_types_to_fix
from property_return import property_return_types_to_fix
from additional_properties import additional_properties_list


def fixInputTypes(
    class_name: str,
    obj_name: str,
    input_name: str,
    old_input_type: str,
) -> tuple[str | None, str | None]:
    if get_class := method_inputs_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            if (
                get_obj["input_name"] == input_name
                and get_obj["old_input_type"] == old_input_type
            ):
                return get_obj["input_type"], get_obj["extra_import"]
    return None, None


def fixMethodReturnTypes(
    class_name: str,
    obj_name: str,
    old_return_type: str,
) -> tuple[str | None, str | None]:
    if get_class := method_return_types_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            if get_obj["old_return_type"] == old_return_type:
                return get_obj["return_type"], get_obj["extra_import"]
    return None, None


def fixPropertyReturnTypes(
    class_name: str,
    obj_name: str,
) -> tuple[str | None, str | None]:
    if get_class := property_return_types_to_fix.get(class_name):
        if get_obj := get_class.get(obj_name):
            return get_obj["return_type"], get_obj["extra_import"]
    return None, None
