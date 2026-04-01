DATABASE = "BANK DATABASE.db"
DATABASE_TABLES = ("users", "accounts", "system_logs", "transaction_logs",
                   "savings_acc_details", "spending_acc_details")
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
ERROR_CODES = {
    "INSUFFICIENT_FUNDS": "E001",
    "ACCOUNT_FROZEN": "E002",
    "INVALID_ACCOUNT": "E003",
    "TRANSFER_FAILED": "E004",
    "UNAUTHORIZED": "E005"
}
CRYPTOGRAPHY_KEY = b'8GwsvE_ejfY1cQf4R-N1p42c6tLOexcjkqXbjKgryes='
