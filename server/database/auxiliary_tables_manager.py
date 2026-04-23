import sqlite3


class AuxiliaryAccountTables:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.savings_table = "savings_acc_details"
        self.spending_table = "spending_acc_details"

    def create_savings_acc_auxiliary_table(self, account_id):
        self.cursor.execute(  # gpt fix start
            f"INSERT INTO {self.savings_table} (account_id) VALUES (?)",
            (account_id,),
        )  # gpt fix end
        self.connection.commit()

    def create_spending_acc_auxiliary_table(self, account_id):
        self.cursor.execute(  # gpt fix start
            f"INSERT INTO {self.spending_table} (account_id) VALUES (?)",
            (account_id,),
        )  # gpt fix end
        self.connection.commit()


'''
Removed lines:
Line 1: from server.config.database import database_config as db_config
Lines 13-15:         self.cursor.execute(
            """fINSERT INTO {self.savings_table} (account_id)
                VALUES ({account_id})""")
Lines 19-21:         self.cursor.execute(
            """fINSERT INTO {self.spending_table} (account_id)
                VALUES ({account_id})""")
Lines 13-17:         self.cursor.execute(  #gpt fix
            """fINSERT INTO {self.savings_table} (account_id)  #gpt fix
                VALUES (?)""",  #gpt fix
            (account_id,),  #gpt fix
        )  #gpt fix
Lines 21-25:         self.cursor.execute(  #gpt fix
            """fINSERT INTO {self.spending_table} (account_id)  #gpt fix
                VALUES (?)""",  #gpt fix
            (account_id,),  #gpt fix
        )  #gpt fix
Line 13:         self.cursor.execute(f"INSERT INTO {self.savings_table} (account_id) VALUES (?)", (account_id,))  
#gpt fix
Line 17:         self.cursor.execute(f"INSERT INTO {self.spending_table} (account_id) VALUES (?)", (account_id,))  
#gpt fix
'''
