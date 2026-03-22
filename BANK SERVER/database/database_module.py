"""


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