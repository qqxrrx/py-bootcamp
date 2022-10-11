def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)


sum_all_values(1, 2, 3, 4, 5)

# tuple unpacking; called_function(*<argument>)
sum_all_values(*[7, 8, 9, 5, 6, 1, 3])
