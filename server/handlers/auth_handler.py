from server.database.database_manager import *
from server.core import core_functions as funcs
from server.core.results import Result


def create_new_user(user_details):
    required_user_details_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS["users"]
    buffer = funcs.validate_dict_schema(required_user_details_schema, user_details)
    if buffer.success:
        _buffer = user.create_new_user(user_details)
        if _buffer.success:
            return Result(success=True)
        else:
            return Result(success=False, error_code=_buffer.error_code, error_message=_buffer.error_message)
    else:
        return Result(success=False, error_code=buffer.error_code, error_message=buffer.error_message)


def login()








"""
def func that creates new users:
    param : user details(optional)
    if user details:
        authenticate shema(firstname, lastname, username, password, ...)
        ensure username is unique
        validate password structure
        hash password+salt and save it, encrypt other user data and save
    else:
        ask for firstname
        ask for lastname
        ask for username
        check if username is available
        ask for password
        validate password structure
        encrypt / hash all data
    auto login

def func for login:
    param : user details(optional)
    if user details:
        validate schema(username, password)
        ensure user exists
        validate password
        call appropriate function for session token
    else:
        ask for username
        validate existence
         ask for password
         validate it
         session token

def func for logout:
    automatically invalidate session token



"""