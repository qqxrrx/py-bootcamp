# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper


# decorator pattern, accept different parameter signatures
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"hi i'm {name}"


@shout
def order(main, side):
    return f"hi, i like the {main}, with side of {side}"


print(greet("maria"))
print(order("egg", "pie"))
