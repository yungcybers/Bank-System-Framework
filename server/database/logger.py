import sqlite3

from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import (
    SystemLogsSchema,
    TransactionLogsSchema,
)   # gpt fix
from server.config.universal_functions import validate_dict_schema
from server.database.account_manager import Accounts  # gpt fix


class SystemLogger:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.system_logger_table_name = "system_logs"
        self.transaction_logger_table_name = "transaction_logs"
        self.connection.row_factory = sqlite3.Row  # gpt fix start
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.connection.cursor()  # gpt fix end

    def take_system_logs(self, activity_details: SystemLogsSchema):
        if validate_dict_schema(db_config.REQUIRED_DATABASE_TABLES_FIELDS["system_logs"], activity_details):
            columns = ", ".join(activity_details.keys())  # gpt fix
            self.cursor.execute(  # gpt fix start
                f"INSERT INTO {self.system_logger_table_name} "
                f"({columns}) "
                f"VALUES ({','.join(['?'] * len(activity_details))})",
                tuple(detail for detail in activity_details.values()),
            )  # gpt fix end
            self.connection.commit()

    def take_transaction_logs(self, activity_details: TransactionLogsSchema):
        if validate_dict_schema(db_config.REQUIRED_DATABASE_TABLES_FIELDS["transaction_logs"], activity_details):
            columns = ", ".join(activity_details.keys())  # gpt fix
            self.cursor.execute(  # gpt fix start
                f"INSERT INTO {self.transaction_logger_table_name} "
                f"({columns}) "
                f"VALUES ({','.join(['?'] * len(activity_details))})",
                tuple(detail for detail in activity_details.values()),
            )  # gpt fix end
            self.connection.commit()

    def retrieve_transaction_history(self, account_number, pin):
        account = Accounts(self.connection)
        account_details = account.retrieve_account_details(account_number, pin)
        if account_details:
            self.cursor.execute(  # gpt fix start
                f"SELECT * FROM {self.transaction_logger_table_name} "
                "WHERE sender_account_id = ? OR receiver_account_id = ?",
                (account_details["account_id"], account_details["account_id"]),
            )  # gpt fix end
            transaction_history = self.cursor.fetchall()
            return [dict(row) for row in transaction_history]  # gpt fix
        raise Exception(  # gpt fix start
            f"Account with account number '{account_number}' can not be found"
        )  # gpt fix end


'''
Removed lines:
Line 13:         self.cursor = cursor
Line 4: from account_manager import Accounts
Line 41:             return transaction_history
Lines 1-5: from server.config.database import database_config as db_config
from server.config.database.database_input_dict_schema import SystemLogsSchema, TransactionLogsSchema
from server.config.universal_functions import validate_dict_schema
from server.database.account_manager import Accounts  #gpt fix
import sqlite3
Lines 13-17:     def __init__(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        self.cursor = cursor
        self.connection = connection
        self.system_logger_table_name = "system_logs"
        self.transaction_logger_table_name = "transaction_logs"
Lines 17-20:             self.cursor.execute(
                f"""INSERT INTO {self.system_logger_table_name} {tuple(field for field in activity_details.keys())}
                    VALUES ({','.join(list('?' * len(activity_details)))})""",
                tuple(detail for detail in activity_details.values()))
Line 23:                 f"{tuple(field for field in activity_details.keys())} "
Lines 25-28:             self.cursor.execute(
                f"""INSERT INTO {self.transaction_logger_table_name} {tuple(field for field in activity_details.keys())}
                    VALUES ({','.join(list('?' * len(activity_details)))})""",
                tuple(detail for detail in activity_details.values()))
Line 33:                 f"{tuple(field for field in activity_details.keys())} "
Lines 35-39:             self.cursor.execute(
                F"""SELECT * FROM {self.transaction_logger_table_name}
                    WHERE sender_account_id = ?
                    OR receiver_account_id = ?""",
                (account_details['account_id'], account_details['account_id']))
Lines 42-43:         else:
            raise Exception(f"Account with account number '{account_number}' can not be found")
'''
