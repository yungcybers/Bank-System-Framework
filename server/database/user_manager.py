import sqlite3

from server.config import universal_functions as funcs
from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import UsersSchema
from server.security import cryptokit  # gpt fix


class User:
    def __init__(self, connection: sqlite3.Connection,):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA foreign_keys = ON;")  # gpt fix

    def create_new_user(self, user_details: UsersSchema):
        required_table_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS["users"]
        funcs.validate_dict_schema(required_table_schema, user_details)
        user_details = dict(user_details)  # gpt fix start
        user_details["password"] = cryptokit.hash_passkey(user_details["password"])  # gpt fix end
        columns = ", ".join(user_details.keys())  # gpt fix

        self.cursor.execute(  # gpt fix start
            f"INSERT INTO users ({columns}) "
            f"VALUES ({','.join(['?'] * len(user_details))})",
            tuple(user_details.values()),
        )  # gpt fix end
        self.connection.commit()
        return True

    def get_user_id(self, username: str):
        self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))  # gpt fix
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

'''
Removed lines:
Lines 16-17:         self.cursor.execute("""fINSERT INTO users {tuple(key for key in user_details.keys())} 
                        VALUES {tuple(value for value in user_details.values())}""")
Line 22:         self.cursor.execute("fSELECT id FROM users WHERE username = '{username}'")
Lines 19-23:         self.cursor.execute(  #gpt fix
            """fINSERT INTO users {tuple(key for key in user_details.keys())}  #gpt fix
                        VALUES ({",".join(["?"] * len(user_details))})""",  #gpt fix
            tuple(user_details.values()),  #gpt fix
        )  #gpt fix
Lines 1-5: from server.config import universal_functions as funcs
from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import UsersSchema
import sqlite3
from server.security import cryptokit  #gpt fix
Line 19:         self.cursor.execute(f"INSERT INTO users {tuple(key for key in user_details.keys())} 
VALUES ({','.join(['?'] * len(user_details))})", tuple(user_details.values()))  #gpt fix
Line 21:             f"INSERT INTO users {tuple(key for key in user_details.keys())} "
'''
