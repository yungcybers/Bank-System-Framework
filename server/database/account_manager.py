import sqlite3

from server.config import universal_functions as funcs
from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import AccountsSchema
from server.security import cryptokit
from server.database import auxiliary_tables_manager  # gpt fix


class Accounts:
    def __init__(self,  connection: sqlite3.Connection):
        self.connection = connection
        self.table = "accounts"
        self.connection.row_factory = sqlite3.Row  # gpt fix start
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.connection.cursor()
        self.auxiliary_tables = auxilliary_tables_manager.AuxiliaryAccountTables(
            self.connection
        )  # gpt fix end

    def create_account(self, account_details: AccountsSchema):
        """
        This is a method for the accounts class that creates a new account.
        It first validates if the schema of the account details dict is right.
        It then ensures that that user does not have an account with that type

        """
        # Remember that the pin must be hashed and all other data encrypted
        account_details = dict(account_details)  # gpt fix start
        columns = ", ".join(account_details.keys())  # gpt fix end
        required_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS[self.table]
        if funcs.validate_dict_schema(required_schema, account_details):
            self.cursor.execute(  # gpt fix start
                f"SELECT * FROM {self.table} WHERE user_id = ? and account_type = ?",
                (account_details["user_id"], account_details["account_type"]),
            )  # gpt fix end
            if not self.cursor.fetchall():
                # checking to ensure that the user does not already have that specific account type
                account_details["pin"] = cryptokit.hash_passkey(account_details["pin"])
                self.cursor.execute(  # gpt fix start
                    f"INSERT INTO {self.table} "
                    f"({columns}) "
                    f"VALUES ({','.join(['?'] * len(account_details))})",
                    tuple(account_details.values()),
                )  # gpt fix end
                self.cursor.execute(  # gpt fix start
                    f"SELECT account_id FROM {self.table} "
                    "WHERE user_id = ? and account_type = ?",
                    (account_details["user_id"], account_details["account_type"]),
                )  # gpt fix end
                account_id = self.cursor.fetchone()["account_id"]  # gpt fix

                if account_details["account_type"] == "SAVINGS":
                    self.auxiliary_tables.create_savings_acc_auxiliary_table(account_id)
                else:
                    self.auxiliary_tables.create_spending_acc_auxiliary_table(account_id)
                self.connection.commit()
                return True
            raise Exception(  # gpt fix start
                f"User with id [{account_details['user_id']}] "
                f"already has a {account_details['account_type']} account"
            )  # gpt fix end

        raise Exception  # gpt fix

    def retrieve_account_details(self, account_number: str, pin: str):
        self.cursor.execute(  # gpt fix start
            f"SELECT * FROM {self.table} WHERE account_number = ?",
            (account_number,),
        )  # gpt fix end
        account_data = self.cursor.fetchone()
        if account_data:
            account_data = dict(account_data)
            assert cryptokit.validate_passkey(pin, account_data["pin"]), "Incorrect pin"
            return account_data
        raise Exception("Account seems to be non existent")  # gpt fix

    def update_user_balance(self, account_number: str, pin: str, new_balance: int):
        self.retrieve_account_details(account_number, pin)  # This is just to validate user existence and pin
        self.cursor.execute(  # gpt fix start
            f"UPDATE {self.table} SET balance = ? WHERE account_number = ?",
            (new_balance, account_number),
        )  # gpt fix end
        self.connection.commit()  # gpt fix
        return True


'''
Removed lines:
Line 12:         self.cursor = cursor
Line 6: import auxiliary_tables_manager
Lines 26-28:             self.cursor.execute("""fSELECT * FROM {self.table} 
                                    WHERE user_id = {account_details['user_id']} and 
                                    account_type = '{account_details['account_type']}'""")
Lines 32-35:                 self.cursor.execute("""f
                        INSERT INTO {self.table} {tuple(key for key in account_details.keys())} 
                        VALUES {tuple(value for value in account_details.values())}
                """)
Line 40:                 account_id = self.cursor.fetchone()
Lines 56-57:         self.cursor.execute("""fSELECT * FROM {self.table} 
                                WHERE account_number = '{account_number}'""")
Lines 68-71:         self.cursor.execute("""fUPDATE {self.table}
                                SET balance = {new_balance}
                                WHERE account_number = '{account_number}'
                            """)
Lines 28-33:             self.cursor.execute(  #gpt fix
                """fSELECT * FROM {self.table}  #gpt fix
                                    WHERE user_id = ? and  #gpt fix
                                    account_type = ?""",  #gpt fix
                (account_details["user_id"], account_details["account_type"]),  #gpt fix
            )  #gpt fix
Lines 37-43:                 self.cursor.execute(  #gpt fix
                    """f  #gpt fix
                        INSERT INTO {self.table} {tuple(key for key in account_details.keys())}  #gpt fix
                        VALUES ({",".join(["?"] * len(account_details))})  #gpt fix
                """,  #gpt fix
                    tuple(account_details.values()),  #gpt fix
                )  #gpt fix
Lines 64-68:         self.cursor.execute(  #gpt fix
            """fSELECT * FROM {self.table}  #gpt fix
                                WHERE account_number = ?""",  #gpt fix
            (account_number,),  #gpt fix
        )  #gpt fix
Lines 79-85:         self.cursor.execute(  #gpt fix
            """fUPDATE {self.table}  #gpt fix
                                SET balance = ?  #gpt fix
                                WHERE account_number = ?  #gpt fix
                            """,  #gpt fix
            (new_balance, account_number),  #gpt fix
        )  #gpt fix
Lines 1-6: from server.config import universal_functions as funcs
from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import AccountsSchema
import sqlite3
from server.security import cryptokit
from server.database import auxilliary_tables_manager  #gpt fix
Line 13:         self.auxiliary_tables = auxilliary_tables_manager.AuxiliaryAccountTables(self.cursor, self.connection)
Line 28:             self.cursor.execute(f"SELECT * FROM {self.table} 
WHERE user_id = ? and account_type = ?", (account_details["user_id"], account_details["account_type"]))  #gpt fix
Line 32:                 self.cursor.execute(f"INSERT INTO {self.table} {tuple(key for key in account_details.keys())} 
VALUES ({','.join(['?'] * len(account_details))})", tuple(account_details.values()))  #gpt fix
Lines 12-19:         self.cursor = cursor
        self.connection = connection
        self.auxiliary_tables = auxilliary_tables_manager.AuxiliaryAccountTables(  # gpt fix start
            self.cursor, self.connection
        )  # gpt fix end
        self.table = "accounts"
        self.connection.row_factory = sqlite3.Row  # gpt fix start
        self.cursor = self.connection.cursor()  # gpt fix end
Line 29:         required_schema = db_config.REQUIRED_DATABASE_TABLES_FIELDS[self.table]
Line 40:                     f"{tuple(key for key in account_details.keys())} "
Lines 33-36:                 self.cursor.execute(f"""SELECT account_id FROM {self.table}
                                       WHERE user_id = ? and 
                                       account_type = ? """,
                                    (account_details['user_id'], account_details['account_type']))
Lines 45-47:             else:
                raise Exception(f"User with id [{account_details['user_id']}] "
                                f"already has a {account_details['account_type']} account")
Lines 49-50:         else:
            raise Exception
Line 53:         self.cursor.execute(f"SELECT * FROM {self.table} WHERE account_number = ?", (account_number,))  
#gpt fix
Lines 59-60:         else:
            raise Exception("Account seems to be non existent")
Line 64:         self.cursor.execute(f"UPDATE {self.table} SET balance = ? WHERE account_number = ?", 
(new_balance, account_number))  #gpt fix
'''
