name = "abcde"  # an iterable by default

# using iter(...) returns an iterator where we should call next(...) to manually loop on elements
it = iter(name)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
