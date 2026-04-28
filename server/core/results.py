class Result:
    def __init__(self, success: bool, data=None, error_code=None, error_message=None):
        self.success = success
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
