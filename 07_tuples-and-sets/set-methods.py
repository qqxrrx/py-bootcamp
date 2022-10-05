print("\n.add()")
s = set([1, 2, 3])
print(s)
s.add(4)
s.add(1)
print(s)


print("\n.remove() and .discard()")
s = {1, 2, 3, 4, 5, 6}
print(s)
s.remove(6)
# s.remove(7) # KeyError!
# alternative is use .discard()
s.discard(7)
print(s)


print("\n.copy()")
s = set([1, 2, 3])
s2 = s.copy()
print(f"(s == s2) {s == s2}")
print(f"(s is s2) {s is s2}")


print("\n.clear()")
s = set([7, 8, 9, 10])
print(s)
s.clear()
print(s)  # return empty set
print(type(s))
