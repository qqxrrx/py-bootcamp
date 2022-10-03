# slicing
# uses : for slicing
# list[<start index>:<end index>:<step value>]
# slicing returns it's own version of the list, the original list is untouched
#   creates a new copy, therefore they reside in different memory address
# <end index> is exclusive (not included)
# <step value> step, just like .range()

items = [1, 2, 3, 4]
print("\n<start index>")
print(items)
print(items[1:])  # start at index 1
print(items[3:])  # start at index 3

# <start index> negative number will move backwards
print(items[-1:])  # start at last index
print(items[-3:])  # start at last index and move backwards

print(items[:])  # return all items


items = ["a", "b", "c", "d", "e", "f"]
print("\n<end index>")
print(items)
print(items[:2])  # start at index zero, include up to index 1
print(items[:4])  # start at index zero, include up to index 3
print(items[1:3])  # start at index 1, include upto index 2
print(items[:-1])  # start at index zero, include up to index before last index
print(items[1:-1])  # start at index 1, include up to index before last index


print("\n<step value>")
print(items)
print(items[1::2])  # start at index 1, step every 2
print(items[::2])  # start at index 0, up to last index, step every 2

# start at index 1, up to last index, step 1 backwards using start index as reference
print(items[1::-1])

# start at index 0, up to index 1, but step backwards starting from last index upto before indicated <end index>
print(items[:1:-1])

# start at index 2, then step backwards including <start index>
print(items[2::-1])


str = "the quick brown fox jumped over the lazy dog"
print("\nreverse string")
print(str)
print(str[::-1])


num = [1, 2, 3, 4, 5]
print("\nmodify portion of strings")
# start at index 0, up to index 2... then replace that position with the list of strings
num[1:3] = ['a', 'b', 'c']
print(num)


txt = ["maria", "alucard", "richter"]
print("\naccess list item, then reverse string")
ans = txt[1][::-1]
print(ans)
# string manipulation
print(ans[0])
print(ans[::2])


pets = ["cat", "dog"]
print("\nswapping of list items")
print(pets)
pets[0], pets[1] = pets[1], pets[0]
print(pets)
