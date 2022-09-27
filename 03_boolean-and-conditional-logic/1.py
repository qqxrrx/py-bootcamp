data = input("fave color?: ")
print(f"your answer was: \"{data}\"")


# in javascript to python
# .toLowerCase() = .lower()
# .trim() = .strip()
if data.lower().strip() == "red":
    print("that's a good color")
elif data.lower().strip() == "black":
    print("that's a fine color too")
elif data.lower().strip() == "indigo":
    print("rare color")
elif data.lower().strip() == "green":
    print("color of nature")
else:
    print("bad color")
