try:
    # nonexistingvariable   # uncomment
    pass
except:
    print("problem")


try:
    # nonexistingvariable   # uncomment
    pass
except NameError as e:  # specify an error type that is expected
    print(e)


def getValue(d, key):
    try:
        return d[key]
    except KeyError:
        return None


x = {"a": "b"}
print(getValue(x, "xx"))
