from server.config import universal_functions as funcs
from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import AccountsSchema
import sqlite3
from server.security import cryptokit


class Accounts:
    def __init__(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        self.cursor = cursor
        self.connection = connection
        self.table = "accounts"

    def create_account(self, account_details: AccountsSchema):
        """
        This is a method for the accounts class that creates a new account.
        It first validates if the schema of the account details dict is right.
        It then ensures that that user does not have an account with that type

        """
        # Remember that the pin must be hashed and all other data encrypted
        required_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS[self.table]
        if funcs.validate_dict_schema(required_schema, account_details):
            self.cursor.execute(f"""SELECT * FROM {self.table} 
                                    WHERE user_id = {account_details['user_id']} and 
                                    account_type = '{account_details['account_type']}'""")
            if not self.cursor.fetchall():
                # checking to ensure that the user does not already have that specific account type
                account_details["pin"] = cryptokit.hash_passkey(account_details["pin"])
                self.cursor.execute(f"""
                        INSERT INTO {self.table} {tuple(key for key in account_details.keys())} 
                        VALUES {tuple(value for value in account_details.values())}
                """)
                self.connection.commit()
                return True
            else:
                raise Exception(f"User with id [{account_details['user_id']}] "
                                f"already has a {account_details['account_type']} account")

        else:
            raise Exception

    def retrieve_account_details(self, account_number: str, pin: str):
        self.cursor.execute(f"""SELECT * FROM {self.table} 
                                WHERE account_number = '{account_number}'""")
        account_data = self.cursor.fetchone()
        if account_data:
            account_data = dict(account_data)
            assert cryptokit.validate_passkey(pin, account_data["pin"]), "Incorrect pin"
            return account_data
        else:
            raise Exception("Account seems to be non existent")

    def update_user_balance(self, account_number: str, pin: str, new_balance: int):
        self.retrieve_account_details(account_number, pin)  # This is just to validate user existence and pin
        self.cursor.execute(f"""UPDATE {self.table}
                                SET balance = {new_balance}
                                WHERE account_number = '{account_number}'
                            """)
        return True




"""
define func for making new account:
    param : acc_type, user_id, user_password, account pin
    check if user exists
    validate password
    buffer the account table for the specific account type
    confirm that the user doesn't already have an account
    raise error is user already has an account
    create new account with default balance 0
    hash the pin + salt and save both hashed pin and the salt

define func for retrieving account balance:
    param : acc_type, user_id, account_pin
    open specific table based on the acc_type
    find user's account details using user_id
    validate user using pin
    display ACCESS DENIED ERROR if pin is wrong
    retrieve and decrypt user's balance
    return user's balance in int

define func for editing user balance:
    param : acc_type, user_id, account_pin
    buffer specific table based on acc_type
    validate access by ensuring that the pin entered + salt hashed is the same as the hashed password stored
    display ACCESS DENIED ERROR if pin is wrong
    encrypt and enter the new balance if pin is right
    return True



"""
