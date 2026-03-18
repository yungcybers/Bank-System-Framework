"""
define func for finding a user:
    param : user id
    enter users table
    check for user with that id
    decrypt user
    return that user as a dict


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

define func for making new user:
    param : user_details(dict)
    confirm the format (first_name, last_name, username, password)
    check to ensure no user has that username
    encrypt the user and write it into the users table
    hash the password + salt and store hashed password and salt
    return True

define func for making new account:
    param : acc_type, user_id, user_password, account pin
    check if user exists
    validate password
    buffer the account table for the specific account type
    confirm that the user doesn't already have an account
    raise error is user already has an account
    create new account with default balance 0
    hash the pin + salt and save both hashed pin and the salt


define func that takes logs of all general activities:
    param : activity_details(dict)
    validate that the activity_details dict has the right format. (activity, timestamp)
    encrypt and write it in a logs table

define func that takes logs of all account activities:
    param : activity_details(dict)
    validate that the activity_details dict has the right format.
    (transaction_type, sender_id, reciepient_id, amount, transaction id, transaction status, new_sender/rece_balance)
    encrypt and write into a transactional logs table
    send message into receipient and sender inboxes

define func that lets users retrieve transaction history:
    param : user_id, user_password
    validate the user via the password
    retrieve and decrypt all logs from transactional logs table that involve the user
    return logs as a list of dicts






"""