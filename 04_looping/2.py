
print("\n-- 1 --")
# generate 9 digits, starting at 0
count = 9
for i in range(count):
    print(f"{i} of {count-1}")


print("\n-- 2 --")
# start at 10
# until 20
for i in range(10, 21):
    print(i)


print("\n-- 3 --")
# start at 2
# until 20
# step up, 2 per step
for i in range(2, 21, 2):
    print(i)


# start at 10
# until 1
# step down, -1 per step
print("\n-- 4 --")
for i in range(10, 0, -1):
    print(i)
