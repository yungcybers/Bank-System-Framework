"""
define func for finding a user:
    param : user id
    enter users table
    check for user with that id
    decrypt user
    return that user as a dict

define func for making new user:
    param : user_details(dict)
    confirm the format (first_name, last_name, username, password)
    check to ensure no user has that username
    encrypt the user and write it into the users table
    hash the password + salt and store hashed password and salt
    return True

"""