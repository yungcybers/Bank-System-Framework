from server.config.database import database_config as db_config
import account_manager
import sqlite3

connection = sqlite3.connect(db_config.DATABASE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

idek = account_manager.Accounts(cursor, connection)
print(idek.retrieve_account_details("12345", "1111"))


def validate_database_schema():
    cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table';""")
    existent_tables = cursor.fetchall()
    formated_table = []

    for table_tuple in existent_tables:
        formated_table.append(table_tuple[0])

    missing_tables = []

    for table in db_config.DATABASE_TABLES:
        if table not in formated_table:
            missing_tables.append(table)

    if missing_tables:
        raise RuntimeError(f"Missing tables: {missing_tables}")


