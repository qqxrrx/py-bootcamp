nums = [7, 3, 1, 56, 42, 21, 66]
print(sorted(nums))
print(sorted(nums, reverse=True))  # reverse order


tups = (76, 3, 4, 12, 45, 12, 77)  # tuples
print(sorted(tups))


users = [{"usr": 'Ffff', "tweets": []},
         {"usr": 'Aaaa', "tweets": ["1", "2", "3", "4"]},
         {"usr": 'Eeee', "tweets": ["5", "6", "x"]},
         {"usr": 'Cccc', "tweets": [], "num": 42, "color":"violet"},
         {"usr": 'Bbbb', "tweets": ["3", "4"]},
         {"usr": 'Dddd', "tweets": [], "num": 10, "color":"red"}]

# sort by number of keys
print("\nkey=len")
print(sorted(users, key=len))

# sort based on 'usr' key
print("\nkey='usr'")
print(sorted(users, key=lambda user: user['usr']))

# sort based on 'tweets' length
print("\nkey='tweets'")
print(sorted(users, key=lambda user: len(user['tweets'])))


songs = [{"title": "song1", "playcount": 1},
         {"title": "song2", "playcount": 6},
         {"title": "song3", "playcount": 99},
         {"title": "song4", "playcount": 31}, ]

# sort based on 'playcount' key (with most plays first)
print("\nkey='playcount'")
print(sorted(songs, key=lambda s: s['playcount'], reverse=True))
