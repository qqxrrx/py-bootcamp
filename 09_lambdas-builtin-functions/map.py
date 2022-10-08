nums = [1, 2, 3, 4, 5]

doubles = list(map(lambda n: n*2, nums))
print(doubles)

members = ['a', 'b', 'c']
member2 = list(map(lambda n: n.upper(), members))
print(member2)

names = [{'fn': 'A1', 'ln': 'A2'},
         {'fn': 'B1', 'ln': 'B2'},
         {'fn': 'B1', 'ln': 'B2'}]

fns = list(map(lambda n: n['fn'], names))
print(fns)

# just use list comprehension for simple use cases
print([n['fn'] for n in names])
