item = {
    "name": "john doe",
    "found_purpose": True,
    "num_of_dreams": 100,
}

print("\ntest if key exists")
print("name" in item)
print("100" in item)

print("\ntest if value exists")
print("john doe" in item.values())
print(False in item.values())
print(True in item.values())
