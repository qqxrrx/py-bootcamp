# .clear() remove all items from list
print("\n.clear()")
items = [1, 2, 3, 4]
print(items)
items.clear()
print(items)


# .pop(<zero-based-index>) pass index where you want to delete an item
# no argument = remove last item by default
print("\n.pop()")
items = [1, 2, 3, 4]
items.pop(0)
print(items)
items.pop()
print(items)


# .remove(<value to remove>) pass value, and remove 1st occurance
print("\n.remove()")
items = ["a", "b", 3, True, False, True, False]
print(items)
items.remove(False)
print(items)
