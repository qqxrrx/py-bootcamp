from functools import wraps


def log_function_data(fn):
    # ensures that the function being decorated, it's metadata is not lost
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """WRAPPER FUNCTION"""
        print(f"calling function: {fn.__name__}")
        print(f"documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """adds two numbers"""
    return x+y


print(add.__doc__)
print(add.__name__)
help(add)
