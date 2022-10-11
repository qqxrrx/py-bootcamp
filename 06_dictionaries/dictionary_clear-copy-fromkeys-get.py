print("\n.clear()")
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(f"d.clear(): {d}")


print("\n.copy()")
d = dict(a=1, b=2, c=3)
c = d.copy()
print(c)
print(f"is c has equal value to d?: {c == d}")
print(f"is c identical to d?: {c is d}")


# create key-value pair
# from separated values of an
# iterable collection
# used to generate default values
print("\n.fromkeys()")
print({}.fromkeys("a,b"))
print({}.fromkeys(["email", "name", "score"], "unknown"))
print({}.fromkeys("a", [1, 2, 3, 4, 5]))
# each character got iterated, only uses unique characters as key
print({}.fromkeys("test", "unknown"))
print({}.fromkeys(range(1, 10), 'unknown'))


print("\n.get()")
d = dict(a=4, b=3, c=2, d=1)
print(d.get('a'))
print(d['a'])

print(d.get('e'))  # this will have no error, just returns 'None'
print(d['e'])  # KeyValue error
