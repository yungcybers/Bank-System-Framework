from .results import Result


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
                errors.append({
                    key: f"Expected type ({expected_type_name}) but got ({type(dict_to_be_validated[key]).__name__})"
                })
        else:
            errors.append({key: "Key not found"})

    if errors:
        return Result(success=False, error_code="E010", error_message=errors)
    else:
        return Result(success=True)
