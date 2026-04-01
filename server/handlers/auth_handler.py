"""
def func that creates new users:
    param : user details(optional)
    if user details:
        authenticate shema(firstname, lastname, username, password, ...)
        ensure username is unique
        validate password structure
        hash password+salt and save it, encrypt other user data and save
    else:
        ask for firstname
        ask for lastname
        ask for username
        check if username is available
        ask for password
        validate password structure
        encrypt / hash all data
    auto login

def func for login:
    param : user details(optional)
    if user details:
        validate schema(username, password)
        ensure user exists
        validate password
        call appropriate function for session token
    else:
        ask for username
        validate existence
         ask for password
         validate it
         session token

def func for logout:
    automatically invalidate session token



"""