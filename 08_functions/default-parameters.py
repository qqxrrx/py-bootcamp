def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))
print(exponent(3, 2))
print(exponent(3))
print(exponent(7))


def add(a=10, b=20):
    return a+b


print(add())
print(add(1, 10))


print("can use a function parameter")


def subtract(a, b):
    return a-b


def math(a, b, fn=add):
    return fn(a, b)


print(math(2, 2))
print(math(2, 2, subtract))
