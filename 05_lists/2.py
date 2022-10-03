list_items = []
answer = None
while True:
    answer = input("give a list value, 'q' to quit: ")
    if answer == 'q':
        break
    list_items.append(answer)

if len(list_items) > 0:
    print(list_items)


# turn range() to a list:
print(list(range(1, 10)))
