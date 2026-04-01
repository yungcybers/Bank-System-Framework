from server.config import database_config as db_config
import sqlite3

connection = sqlite3.connect(db_config.DATABASE)
print("Connecting to database......\n Connection established!!! \n Creating cursor......"
      "\nLoading tables.....\nChecking for missing tables\nDatabase initialised successfully")
cursor = connection.cursor()

cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table';""")
print()

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

