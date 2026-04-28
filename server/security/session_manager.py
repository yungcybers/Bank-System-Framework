import secrets
import datetime
from server.core import core_functions as funcs
from server.config.database import database_config as db_config
from server.database import database_manager
from server.core.results import Result


def generate_session_token():
    return secrets.token_urlsafe(32)


def start_new_session(user_id: int):
    session_token = generate_session_token()
    required_session_details_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS["sessions"]
    session_details = {"session_token": session_token,
                       "user_id": user_id,
                       "created_at": datetime.datetime.today(),
                       "ends_at": datetime.datetime.today() + datetime.timedelta(minutes=5),
                       "status": "active"}
    buffer = funcs.validate_dict_schema(required_session_details_schema, session_details)
    if buffer.success:
        _buffer = database_manager.sessions.new_session(session_details)
        if _buffer.success:
            return Result(success=True)
        else:
            return Result(success=False, error_code=_buffer.error_code, error_message=_buffer.error_message)
    else:
        return Result(success=False, error_message=buffer.error_message, error_code=buffer.error_code)







"""
def func for generating session tokens
    just generate and return the session token

def func for starts a session :
    param : user id
    generate a session token
    save the session token to the table for sessions

def func that ends session:
    param : session token
    change status to ended


FIND A WAY TO ENSURE A THREAD IS RUNNING THAT GOES THROUGH AND UPDATES STATUS AFTER EVERY 20 SECONDS
"""
