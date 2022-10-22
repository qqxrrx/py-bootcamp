import time


def nums():
    for num in range(1, 10):
        yield num


# g = nums()
# next(g)

# generator expression:
g = (num for num in range(1, 10))


# [...] = list comprehension
# {k:v...} = dictionary comprehension
# {...} = set comprehension
# (...) = generator expression

# (a,b,c,d) = tuple (read only, faster than set)
# {a,b,c,d} = set (all unique)
# {k:v} = dictionary (key-value pair)
# [a,b,c,d] = list


# ---- speed testing :
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_time = time.time() - list_start_time

print(f"sum(n for n in range(10000000)): {gen_time}")
print(f"sum([n for n in range(10000000)]): {list_time}")
# --------------------
