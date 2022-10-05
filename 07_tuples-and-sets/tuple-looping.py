letters = ('h', 'e', 'y')

for letter in letters:
    print(letter)


i = len(letters) - 1

while i >= 0:
    print(letters[i])
    i -= 1


print("\n.count()")
tup = tuple([1, 1, 1, 12, 2, 2, 2, 23, 2, 4, 4, 24, 24, 24, 552])
print(f"tup: {tup}")
print(f"tup.count(1): {tup.count(1)}")
print(f"tup.count(4): {tup.count(4)}")
print(f"tup.count(24): {tup.count(24)}")
print(f"tup.count(0): {tup.count(0)}")



print("\n.index(), 1st occurance")
print(f"tup: {tup}")
print(f"tup.index(552): {tup.index(552)}")
print(f"tup.index(4): {tup.index(4)}")

if 999 in tup:
    # ValueError if not for the if statement
    print(f"tup.index(999): {tup.index(999)}")
