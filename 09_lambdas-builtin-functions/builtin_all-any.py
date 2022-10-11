# return True if all statements of iterable are truthy
print("\n.all()")

print(all([0, 1, 2, 3]))
print(all([1, 1, 1, 1]))
print(all([char for char in 'eio' if char in 'aeiou']))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


# return True if ANY statements of iterable are truthy
print("\n.any()")
print(any([0, 1, 2, 3]))
print(any([1, 1, 1, 1]))
print(all([char for char in 'eio' if char in 'ozsplj']))
print(any([num for num in [4, 2, 10, 6, 8, 7, 77, 777] if num % 2 == 0]))
