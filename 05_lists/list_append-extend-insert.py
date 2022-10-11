# .append() = add item to end of list
# just like Array.prototype.push() of javascript
print("\n.append()")
items = [1, 2, 3]
items.append(4)
print(items)


# .extend() = add at the end of list all values
# just like Array.prototype.concat() of javascript but changes the actual list
print("\n.extend()")
items.extend([5, 6, 7])
print(items)


# .insert(<zero-based-index>,<data>) = insert at given position
print("\n.insert()")
items.insert(4, "yo")
print(items)


# note = if you use -1 to insert at end of list it will use the old length, therefore will be inserted at 2nd last
# the solution is:
items.insert(len(items), "end of list")
print(items)
