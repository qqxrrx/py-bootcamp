from functools import wraps


# decorator(<passed-decorator-argument>)(<function-to-wrap-in-decorator>)
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # is the first argument not equal to the argument?
            if args and args[0] != val:
                return f"first arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)


print(fav_foods("burrito", "ice cream"))
print(fav_foods("ice cream", "burrito"))


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1+num2


print(add_to_ten(10, 12))
print(add_to_ten(1, 2))
