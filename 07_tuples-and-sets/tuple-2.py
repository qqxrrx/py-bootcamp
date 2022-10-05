tup1 = (1, 2, 3, 3, 3)

print(tup1[1])
print(tup1[2])
print(tup1[-1])

tup2 = tuple([4, 3, 2])
print(tup2[0])
print(tup2[-1])


print("\n\nusing tuple as dictionary key")
locations = {
    (32.4242, 42.123): "LOCATION 1",
    (40.2132, 2.3231): "LOCATION 2",
    (44.1231, 5.2525): "LOCATION 3"
}
print(locations)

print("\ndict.items() returns a list of tuple of key-value pair")
cat = dict(name="biscuit", age=0.5, favorite_toy="ball")
print(cat.items())
