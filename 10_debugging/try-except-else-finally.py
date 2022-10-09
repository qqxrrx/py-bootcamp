# try:
# except:
# else:
# finally:

while True:
    try:
        num = int(input("enter a number: "))
    except ValueError:   # catch exception
        print("not a number, enter a number again")
    else:     # executed if no exception is encountered
        print("in the else block")
        print(f"{num} input correct")
        break
    finally:  # always run no matter what
        print("last part of code")
print("-- loop exited --")


def divide(a, b):
    try:
        result = a/b
    # except ZeroDivisionError:
    #     return "don't divide by zero"
    # except TypeError as e:
    #     print(e)
    #     return "a and b must be ints or floats only"
    except (ZeroDivisionError, TypeError) as e:
        print(e)
        print("something went wrong")
    else:
        return f"{a} divided by {b} is {result}"


print(f"\n{divide(1, 2)}")
print(f"\n{divide(1, 0)}")
print(f"\n{divide('a', 'b')}")
