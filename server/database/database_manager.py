from server import config
import sqlite3

connection = sqlite3.connect(config.DATABASE)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

"""cursor.execute(
    ""CREATE TABLE transaction_logs (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_account_id INTEGER NOT NULL,
        receiver_account_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        transaction_type TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    )""
)
"""

cursor.execute(
    f"""CREATE TABLE transaction_logs (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_account_id INTEGER,
        receiver_account_id INTEGER,
        amount REAL NOT NULL,
        transaction_type TEXT NOT NULL CHECK(transaction_type IN {config.TRANSACTION_TYPES}),
        status TEXT NOT NULL CHECK(status IN {config.TRANSACTION_STATUS}),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    )"""
)

cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table';""")

existent_tables = cursor.fetchall()
print(existent_tables)
formated_table = []

for table_tuple in existent_tables:
    formated_table.append(table_tuple[0])

missing_tables = []

for table in config.DATABASE_TABLES:
    if table not in formated_table:
        missing_tables.append(table)

if missing_tables:
    raise RuntimeError(f"Missing tables: {missing_tables}")


"""
import config
load database
check for tables(users, spending_acc, main_acc, logs, transactional logs, etc)




"""

"""CREATE TABLE transaction_logs (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    sender_account TEXT,
    receiver_account TEXT,
    amount REAL NOT NULL,
    transaction_type TEXT NOT NULL,
    status TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
)"""
