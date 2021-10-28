def print_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print('Caught this error: ' + repr(error))
    return wrapper
