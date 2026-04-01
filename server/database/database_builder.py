from server.config import database_config as db_config
import sqlite3

connection = sqlite3.connect(db_config.DATABASE)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")


def main():
    cursor.execute(
        """CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                sur_name TEXT NOT NULL,
                password TEXT NOT NULL,
                time_of_creation DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )"""
    )

    cursor.execute(
        """CREATE TABLE system_logs(
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER DEFAULT 0000000000,
        action TEXT NOT NULL,
        description TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

)"""
    )

    cursor.execute(
        """
CREATE TABLE accounts(
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number TEXT UNIQUE NOT NULL,
            user_id INTEGER NOT NULL,
            account_type TEXT CHECK(account_type IN ('SAVINGS', 'SPENDING')),
            balance REAL NOT NULL DEFAULT 0.00,
            date_of_creation DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL  CHECK(status IN ('ACTIVE', 'DORMANT', 'FROZEN', 'CLOSED')),
            last_used DATETIME DEFAULT NULL,
            
            FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE
            )"""
    )

    cursor.execute(
        """CREATE TABLE savings_acc_details(
            account_id INTEGER PRIMARY KEY,
            interest_rate REAL NOT NULL DEFAULT 0.00,
            interest_due_date DATETIME DEFAULT NULL,
            
            FOREIGN KEY (account_id)
            REFERENCES accounts(account_id)
            ON DELETE CASCADE
            
            )"""
    )

    cursor.execute(
        """CREATE TABLE spending_acc_details(
            account_id INTEGER PRIMARY KEY,
            daily_limit REAL DEFAULT 0.00,
            
            FOREIGN KEY (account_id) 
            REFERENCES accounts(account_id)
            ON DELETE CASCADE
            )"""
    )

    cursor.execute(
        f"""CREATE TABLE transaction_logs (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_account_id INTEGER DEFAULT NULL,
            receiver_account_id INTEGER DEFAULT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL CHECK(transaction_type IN {db_config.TRANSACTION_TYPES}),
            status TEXT NOT NULL CHECK(status IN {db_config.TRANSACTION_STATUS}),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (sender_account_id) REFERENCES accounts(account_id) ON DELETE CASCADE,
            FOREIGN KEY (receiver_account_id) REFERENCES accounts(account_id) ON DELETE CASCADE,
            CHECK (
        (transaction_type = 'DEPOSIT' AND sender_account_id IS NULL) OR
        (transaction_type = 'WITHDRAWAL' AND receiver_account_id IS NULL) OR
        (transaction_type = 'TRANSFER' AND sender_account_id IS NOT NULL AND receiver_account_id IS NOT NULL)
    )
        )"""
    )


if __name__ == "__main__":
    main()
