
a = [1, 2, 3]
b = [1, 2, 3]

# objects and arrays are stored in the heap, therefore they reside in a different memory address eventhouh they contain the same value
print(f"array test: {a is b}")

c = a
print(f"assigned array test: {c is a}")

x = 4
y = 4
# primitive types are stored in the stack
print(f"int test:  {x is y}")


# heap = compare memory address
# stack = compare value
