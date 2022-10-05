s = set({1, 2, 3, 4, 4, 4, 4, 5, 5, 5, False, False,
        True, True, (1, 2, 3), "testing set"})
print(type(s))
print(s)  # automatically remove duplicates
print(4 in s)  # using 'in' to check if value exists

for i in s:
    print(i)


numbers = [1, 2, 3, 4, 5, 6, 4, 43, 2, 2, 4, 1, 2, 5, 6, 42, 42, 42, 123]
print("\nremove duplicates on a list:")
print(numbers)
print(f"list(set(numbers)): {list(set(numbers))}")
