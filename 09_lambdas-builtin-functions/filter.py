i = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, i))
print(evens)


names = ['Aa', 'Ab', 'Bb', 'Cc', 'De', 'ae']
new_names = list(filter(lambda n: n[0].lower() == 'a', names))
print(new_names)

# just use list comprehension for simple use cases
print([n for n in names if n[0].lower() == 'a'])


users = [{"usr": 'Aaaa', "tweets": ["1", "2"]},
         {"usr": 'Bbbb', "tweets": ["3", "4"]},
         {"usr": 'Cccc', "tweets": []},
         {"usr": 'Dddd', "tweets": []},
         {"usr": 'Eeee', "tweets": ["5", "6"]},
         {"usr": 'Ffff', "tweets": []}, ]


# empty list is falsy
inactive_users = list(filter(lambda n: not n['tweets'], users))
print(inactive_users)

print(list(map(lambda usr: usr['usr'].upper(),
      filter(lambda u: not u['tweets'], users))))

# better to use list comprehension
print([user for user in users if not user["tweets"]])


print("\ncombine filter and map")
names = ['Nassie', 'Bolt', 'Custy']
print(list(map(lambda name: f"your teacher is {name}",
      filter(lambda value: len(value) < 5, names))))

print("\nlist comprehension:")
print([f"your teacher is {n}" for n in names if len(n) < 5])
