def validate_dict_schema(required_dict_format, dict_to_be_validated):
    errors = []
    for key, value in required_dict_format.items():
        if key in dict_to_be_validated.keys():
            expected_value_type = required_dict_format[key]
            if isinstance(dict_to_be_validated[key], expected_value_type):
                pass
            else:
                if isinstance(expected_value_type, tuple):  # gpt fix start
                    expected_type_name = " or ".join(
                        value_type.__name__ for value_type in expected_value_type
                    )
                else:
                    expected_type_name = expected_value_type.__name__
                errors.append(
                    {
                        key: f"Expected type ({expected_type_name})"
                        f" but got ({type(dict_to_be_validated[key])})"
                    }
                )  # gpt fix end
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


'''
Removed lines:
Lines 12-13:                 errors.append({key: f"Expected type ({expected_value_type.__name__})"
                                    f" but got ({type(dict_to_be_validated[key])})"})
'''
