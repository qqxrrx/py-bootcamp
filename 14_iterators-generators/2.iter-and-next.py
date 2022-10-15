# custom for loop
def my_for(iterable, func):
    # iter() returns an iterator
    iterator = iter(iterable)
    while True:
        try:
            # iterator needs to be called with next() to start looping over
            i = next(iterator)
        except StopIteration:
            print("- end of iterator -")
            break
        else:
            func(i)


def square(x):
    print(x*x)


my_for("abcd", print)
my_for([1, 2, 3, 4], square)
