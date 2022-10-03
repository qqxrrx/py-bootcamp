# .index() return the index of specified item in list
# .index(<value of item>)
# .index(<value of item>, <start at index, inclusive>)
# .index(<value of item>, <start at index, inclusive>, <stop at index>)
print("\n.index()")
num = [1, 2, 3, 4]
print(f"num.index(2): {num.index(2)}")
print(f"num.index(4): {num.index(4)}")
num = [5, 5, 6, 7, 5, 8, 8, 9, 10, 8, 8]
print(f"num.index(5): {num.index(5)}")
print(f"num.index(5, 1): {num.index(5, 1)}")
print(f"num.index(5, 2): {num.index(5, 2)}")
print(f"num.index(8, 6, 8): {num.index(8, 6, 8)}")


# .count(<value of item>) output number of times the input occurs on list
num = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2, False, False, True, True, False, False]
print("\n.count()")
print(num)
value_to_remove = False
for _ in range(num.count(value_to_remove)):
    num.remove(value_to_remove)
print(num)


# .reverse() reverse elements in-place (it will update the current list and not return a new copy)
# this is a reverse operation and not a sort operation
names = ["A4", "B2", "B1", "A2", "A1"]
print("\n.reverse()")
print(names)
names.reverse()
print(names)


# .sort() sort elements in-place (it will update the current list and not return a new copy)
# you can customize sorting
print("\n.sort()")
names = ["A4", "B2", "B1", "A2", "A1"]
print(names)
names.sort()
print(names)


# .join() combines all elements from a list into a string
# a string method, not a list method... but commonly used with lists
# returns combined string from a list
print("\n.join()")
phrase = ["peter", "pipper", "picked", "a", "peck", "of", "pickled", "pepper"]
print(' '.join(phrase))
