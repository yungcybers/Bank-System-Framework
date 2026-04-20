from collections import defaultdict


def validate_dict_schema(required_dict_format, dict_to_be_validated):
    errors = []
    for key, value in required_dict_format.items():
        if key in dict_to_be_validated.keys():
            expected_value_type = required_dict_format[key]
            if isinstance(dict_to_be_validated[key], expected_value_type):
                pass
            else:
                errors.append({key: f"Expected type ({expected_value_type.__name__})"
                                    f" but got ({type(dict_to_be_validated[key])})"})
        else:
            errors.append({key: "Key not found"})

    if errors:
        raise Exception(errors)
    else:
        return True


def generate_dict_for_data_from_list(schema: dict, data_list: list):
    keys = list(schema.keys())
    assert len(keys) == len(data_list)
    assert [isinstance(data_list[x], list(schema.values())[x]) for x in range(len(data_list))], \
        "Values provided in the list do not match the values required in the schema"
    return dict(zip(keys, data_list))
