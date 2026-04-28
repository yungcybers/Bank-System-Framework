from pathlib import Path
from server.core.error_codes_and_exceptions import ERROR_CODES
import datetime

DATABASE = str(Path(__file__).resolve().parents[2] / "database" / "BANK DATABASE.db")
DATABASE_TABLES = ("users", "accounts", "system_logs", "transaction_logs",
                   "savings_acc_details", "spending_acc_details", "sessions")
ACCOUNT_TYPES = ("SAVINGS", "SPENDING")
ACCOUNT_STATUS = ("ACTIVE", "DORMANT", "FROZEN", "CLOSED")
TRANSACTION_TYPES = (
    "DEPOSIT",
    "WITHDRAWAL",
    "TRANSFER",
    "INTEREST",
    "FEE",
    "REVERSAL"
)
TRANSACTION_STATUS = (
    "PENDING",
    "SUCCESS",
    "FAILED",
    "REVERSED"
)
SESSIONS_STATUS = ("active", "ended")
DATABASE_TABLES_FIELDS = {
    "users": ("id", "first_name", "sur_name", "username",  "password", "time_of_creation"),
    "accounts": ("account_id", "account_number", "user_id", "pin",
                 "account_type", "balance", "date_of_creation", "status", "last_used"),
    "system_logs": ("log_id", "user_id", "action", "description", "timestamp"),
    "transaction_logs": ("transaction_id", "sender_account_id",
                         "receiver_account_id", "amount", "transaction_type", "status", "timestamp"),
    "savings_acc_details": ("account_id", "interest_rate", "interest_due_date"),
    "spending_acc_details": ("account_id", "daily_limit"),
    "sessions": ("session_id", "session_token", "user_id", "created_at", "ends_at", "status")
}

REQUIRED_DATABASE_TABLES_FIELDS = {
    "users": {"first_name": str, "sur_name": str, "username": str, "password": str},
    "accounts": {"account_number": str, "user_id": int, "pin": str,
                 "account_type": str},
    "system_logs": {"user_id": int, "action": str, "description": str},
    "transaction_logs": {  # gpt fix start
        "sender_account_id": (int, type(None)),
        "receiver_account_id": (int, type(None)),
        "amount": float,
        "transaction_type": str,
        "status": str,
    },
    "savings_acc_details": {"account_id": int, "interest_rate": float, "interest_due_date": datetime.date},
    "spending_acc_details": {"account_id": int, "daily_limit": float},
    "sessions": {"session_token": str, "user_id": int, "created_at": datetime.datetime,
                 "ends_at": datetime.datetime, "status": str}
}

'''
Removed lines:
Line 3: DATABASE = "BANK DATABASE.db"
Lines 45-46:     "transaction_logs": {"sender_account_id": int, "receiver_account_id": int, "amount": float,
                         "transaction_type": str, "status": str},
'''
