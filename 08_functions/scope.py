print("global variable test --")

total = 0


def inc():
    global total  # need to use 'global' keyword if you want to manipulate a global variable
    total += 1
    return total


print(inc())


txt = "test"


def modify():
    # variable with similar name from global scope only exist within function scope
    txt = "modified"
    return txt


print(modify())
print(txt)


print("nonlocal keyword --")


def outer():
    count = 0

    def inner():
        nonlocal count  # use parent variable from inner function using 'nonlocal' keyword
        count += 1
        return count
    return inner()


print(outer())
