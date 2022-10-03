nums = [1, 2, 3, 4]

# iterating lists
for num in nums:
    print(num)

colors = ["red", "indigo", "black", "green", 1, True, 0.23, ['1', 2, 0.3]]
for c in colors:
    print(c)

for x in list(range(1, 4)):
    print(x*x)


print("\nusing while loop:\n")

letters = ['a', 'x', 'd', 'g', 'z']
i = 0
while i < len(letters):
    print(letters[i])
    i += 1
