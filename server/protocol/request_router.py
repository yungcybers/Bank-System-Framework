from server.protocol.request_parser import *


def route_request(json_request_string: str):
    action, session_token, payload = parse_request(json_request_string_to_dict(json_request_string))



"""
def a func to route requests:
    use the parser from request parser
    determine the required action
    call the appropriate handler
"""