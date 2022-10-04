item = {
    "name": "john doe",
    "found_purpose": True,
    "num_of_dreams": 100,
}

print("\n.values() access:")
for v in item.values():
    print(v)

print("\n.keys() access:")
for k in item.keys():
    print(k)

print("\n.items() access (returns a list of tuples):")
for k, v in item.items():
    print(f"key: {k}\tvalue:{v}")
