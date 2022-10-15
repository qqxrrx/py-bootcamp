# generators are easy way of creating an iterator
def count_up_to(max):
    count = 1
    while count <= max:
        # return 'count' and pause execution until next() is called again
        yield count
        count += 1


# generator object
g = count_up_to(10)
print(f"this is the first next(): {next(g)}")

print("\nproceeding next():")

# for-in loop automatically calls next() and catches the StopIteration error automatically
# StopIteration error is raised if you call next() when there is no more item to iterate to
for n in g:
    print(n)
