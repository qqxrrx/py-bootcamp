print("-- for-loop:")
for i in range(1, 10):
    print("\U0001f600"*i)


print("-- while-loop:")
i = 1
while i < 10:
    print("\U0001f600"*i)
    i += 1


print("-- nested loop:")
for a in range(3):
    for b in range(1, 10):
        print("\U0001f600"*b)


print("-- for + while:")
for num in range(1, 10):
    count = 1
    smiley = ""
    while count <= num:
        smiley += "\U0001f600"
        count += 1
    print(smiley)
