"""
def func that starts the socket
    start tcp socket
    bint socket to server address
    start listening
    spawn thread for each accepted client

def func for handling each client:
    param : client object, client addr, whatever else
    receive data from socket(json str)
    use appropriate func to translate it, this will be true length of the incoming data
    store that len in a variable
    now use that len as the buffer size for the true message
    receive the true message and send it through the right funcs
    ensure that the request is handled
    get the response and send it back


"""