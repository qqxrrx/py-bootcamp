data = input("fave color?: ")
print(f"your answer was: \"{data}\"")


# in javascript to python
# .toLowerCase() = .lower()
# .trim() = .strip()
if data.lower().strip() == "red":
    print("that's a good color")
elif data.lower().strip() == "black":
    print("that's a fine color too")
else:
    print("bad color")
