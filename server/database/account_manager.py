"""
define func for making new account:
    param : acc_type, user_id, user_password, account pin
    check if user exists
    validate password
    buffer the account table for the specific account type
    confirm that the user doesn't already have an account
    raise error is user already has an account
    create new account with default balance 0
    hash the pin + salt and save both hashed pin and the salt

define func for retrieving user balance:
    param : acc_type, user_id, account_pin
    open specific table based on the acc_type
    find user's account details using user_id
    validate user using pin
    display ACCESS DENIED ERROR if pin is wrong
    retrieve and decrypt user's balance
    return user's balance in int

define func for editing user balance:
    param : acc_type, user_id, account_pin
    buffer specific table based on acc_type
    validate access by ensuring that the pin entered + salt hashed is the same as the hashed password stored
    display ACCESS DENIED ERROR if pin is wrong
    encrypt and enter the new balance if pin is right
    return True



"""