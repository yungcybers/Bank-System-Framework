request_dict_schema = {
    "type": str,
    "action": str,
    "session_token": str or None,
    "payload": dict
}

legitimate_actions = ["login", "logout"]
