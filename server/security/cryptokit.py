from cryptography.fernet import Fernet
import bcrypt
from server.core.results import Result

"""KEY_FILE = "Fernet Key.txt"
try:
    with open(KEY_FILE, "r") as file:
        key = file.read()
        key = key.encode()
    cipher = Fernet(key)
except FileNotFoundError:
    with open(KEY_FILE, "w") as file:
        key = Fernet.generate_key()
    cipher = Fernet(key)


def encrypt(data):
    return cipher.encrypt(str(data).encode()).decode()


def encrypt_dict(data: dict):
    assert isinstance(data, dict), f"Expected argument of <class 'dict'>, got {type(data)}"
    for dict_key, value in data.items():
        data[dict_key] = encrypt(value)
    return data


def decrypt(data):
    return cipher.decrypt(str(data).encode()).decode()


def decrypt_dict(data: dict):
    assert isinstance(data, dict), f"Expected argument of <class 'dict'>, got {type(data)}"
    for dict_key, value in data.items():
        data[dict_key] = decrypt(value)
    return data
"""


def hash_passkey(passkey: str):
    hashed_passkey = bcrypt.hashpw(passkey.encode(), bcrypt.gensalt()).decode()
    return Result(success=True, data=hashed_passkey)


def validate_passkey(passkey_to_be_validated: str, stored_hash: str):
    buffer = bcrypt.checkpw(passkey_to_be_validated.encode(), stored_hash.encode())
    if buffer:
        return Result(success=True)
    else:
        error_message = f"Passkey '{passkey_to_be_validated}' is incorrect"
        return Result(success=False, error_code="E009", error_message=error_message)

