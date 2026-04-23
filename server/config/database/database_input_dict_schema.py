"""Generated from database_config.REQUIRED_DATABASE_TABLES_FIELDS.
It generates static Typed dict classes used for typechecking for the various schemas of the dicts required
by the database module when handling input for different tables in the database
"""

import datetime
from typing import TypedDict


class UsersSchema(TypedDict):
    first_name: str
    sur_name: str
    username: str
    password: str


class AccountsSchema(TypedDict):
    account_number: str
    user_id: int
    pin: str
    account_type: str


class SystemLogsSchema(TypedDict):
    user_id: int
    action: str
    description: str


class TransactionLogsSchema(TypedDict):
    sender_account_id: int | None  # gpt fix
    receiver_account_id: int | None  # gpt fix
    amount: float
    transaction_type: str
    status: str

'''
Removed lines:
Lines 31-32:     sender_account_id: int
    receiver_account_id: int
'''


class SavingsAccDetailsSchema(TypedDict):
    account_id: int
    interest_rate: float
    interest_due_date: datetime.date


class SpendingAccDetailsSchema(TypedDict):
    account_id: int
    daily_limit: float
