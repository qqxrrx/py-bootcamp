print("\n.pop()")
d = dict(a=1, b=2, c=3)
print(d)
# requires to provide key or else 'TypeError', if non exisitng key then 'KeyError'
# when we use .pop() it returns the value of the item where .pop() was used
d.pop('a')
print(d)


print("\n.popitem()")
d1 = dict(a=1, b=2, c=3, d=4, e=5)
print(d1)
# .popitem() removes the item that was last inserted into the dictionary
# on python version below v3.7, it removes items randomly
d1.popitem()
print(d1)


print("\n.update()")
first = dict(x=1, y=2, z=3)
second = {"x": "2", "a": "4"}
print(f"first: {first}")
print(f"second: {second}")
# add previous dictionary to this dictionary
# value of a duplicate key will be overwritten
second.update(first)
print(f"updated second: {second}")
