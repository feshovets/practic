import os


def print_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print('Caught this error: ' + repr(error))
    return wrapper


def get_valid_input(prompt="", cast=None, condition=None, error_message=None):
    while True:
        try:
            res = (cast or str)(input(prompt))
            assert condition is None or condition(res)
            return res
        except (ValueError, Exception):
            print(error_message or "Error. Try Again")


def validate_file_path(path):
    if not os.path.exists(path):
        raise ValueError("Non-valid file path")
    return path
