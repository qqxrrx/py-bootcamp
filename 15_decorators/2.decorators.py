print("\ndecorators as functions:")


def be_polite(fn):
    def wrapper():
        print("-- start wrapper() --")
        fn()
        print("-- end wrapper() --")
    return wrapper  # return function


def greet():
    print("hello world (our original function)")


# decorate our greet() function
greet = be_polite(greet)

greet()

# ---------------------------------------------------

print("\nusing @ symbol:")


@be_polite
def greet2():
    print("hello world (using @ symbol)")


greet2()
