"""Generated from database_config.REQUIRED_DATABASE_TABLES_FIELDS."""

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
    sender_account_id: int | None
    receiver_account_id: int | None
    amount: float
    transaction_type: str
    status: str


class SavingsAccDetailsSchema(TypedDict):
    account_id: int
    interest_rate: float
    interest_due_date: datetime.date


class SpendingAccDetailsSchema(TypedDict):
    account_id: int
    daily_limit: float


class SessionsSchema(TypedDict):
    session_token: str
    user_id: int
    created_at: datetime
    ends_at: datetime
    status: str
