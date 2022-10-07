def sum_all_nums(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(sum_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(sum_all_nums(5,4,3,2,1))
