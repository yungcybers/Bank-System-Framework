import json
from server.config.universal_functions import validate_dict_schema
from server.config.protocol import protocol_config


def json_request_string_to_dict(json_string: str):
    converted_json_string: dict = json.loads(json_string)
    return converted_json_string


def parse_request(request: dict):
    validate_dict_schema(protocol_config.request_dict_schema, request)
    assert request["type"] == "request", ("Invalid request, expected request['type'] to be 'request',"
                                          f"got '{request['type']}' instead")
    action = request["action"]
    session_token = request["session_token"]
    payload = request["payload"]
    return action, session_token, payload




"""
def func that converts json string to dict

def func that validates the schema of the dict:
    param : (dict)
    ensures that received dict has the right schema (type, action, token, data)
    returns True

"""