from server.config import universal_functions as funcs
from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import UsersSchema
import sqlite3


class Idek:
    def __init__(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.connection = connection
        self.cursor = cursor

    def create_new_user(self, user_details: UsersSchema):
        required_table_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS["users"]
        funcs.validate_dict_schema(required_table_schema, user_details)

        self.cursor.execute(f"""INSERT INTO users {tuple(key for key in user_details.keys())} 
                        VALUES {tuple(value for value in user_details.values())}""")
        self.connection.commit()
        return True

    def get_user_id(self, username: str):
        self.cursor.execute(f"SELECT id FROM users WHERE username = '{username}'")
        return self.cursor.fetchone()[0]


"""
define func for finding a user:
    param : user id
    enter users table
    check for user with that id
    decrypt user
    return that user as a dict

define func for making new user:
    param : user_details(dict)
    confirm the format (first_name, last_name, username, password)
    check to ensure no user has that username
    encrypt the user and write it into the users table
    hash the password + salt and store hashed password and salt
    return True

"""
