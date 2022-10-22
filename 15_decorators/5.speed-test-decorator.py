from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"executing: {fn.__name__}")
        print(f"time elapsed: {end_time-start_time}")
        return result

    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(5000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(5000000)])


print(f"sum_nums_gen(): {sum_nums_gen()}")
print("\n")
print(f"sum_nums_list(): {sum_nums_list()}")
