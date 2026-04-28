class UserError(Exception):
    pass


class UserNotFoundError(UserError):
    pass


class UsernameUnavailableError(UserError):
    pass


class AccountError(Exception):
    pass


class AccountNotFoundError(AccountError):
    pass


class TransactionError(Exception):
    pass


class InsufficientFundsError(TransactionError):
    pass


class TransactionFailedError(TransactionError):
    pass


class SecurityError(Exception):
    pass


class InvalidPasskeyError(SecurityError):
    pass


class InvalidSessionToken(SecurityError):
    pass


class StructureError(Exception):
    pass


class InvalidDictSchemaError(StructureError):
    pass
