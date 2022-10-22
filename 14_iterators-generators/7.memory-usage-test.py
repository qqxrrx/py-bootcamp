from timeit import timeit


def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums


def fib_gen(max):
    x, y = 0, 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count += 1


for n in fib_list(1000):
    print(n)

# memory wise, use generator
for n in fib_gen(1000):
    print(n)
