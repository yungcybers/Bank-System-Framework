"""
define func that initiates transactions between different users( spending account only):
    param : type, recipient_id, amount, pin
    hash pin+salt and compare to the stored value to authenticate user
    complete transaction
    generate transaction id
    save transaction logs using the appropriate functions

define func that takes logs of transactions between different users:
    param : transaction_details: dict
    validate shema ( transaction_id, time, sender, recipient, new sender balance, new recipient balance)

define func that initiates transaction between two accounts of the same user:
    param : from, to, amount, from_pin
    validate pin
    complete transaction
    generate transaction id
    save transaction logs with the appropriate function

define func that takes logs of transactions between two accounts of the same user:
    param : validate shema ( transaction_id, time, sender_acc, recipient_acc, new sender balance, new recipient balance)

"""