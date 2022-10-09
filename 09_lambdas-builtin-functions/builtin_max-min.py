print('\n.max()')
print(max(88, 24, 55))
print(max('z', 'a', 'e'))  # highest ascii value is 'z'
nums = [40, 11, 425, 22, 12]
print(max(nums))


print('\n.min()')
print(min(88, 24, 55))
print(min('z', 'a', 'e'))  # highest ascii value is 'z'
nums = [40, 11, 425, 22, 12]
print(min(nums))


print('\nshortest name length')
names = ['ben', 'adam', 'jun', 'ada', 'kite']
print(names)
print(min(len(name) for name in names))  # generator
print([len(name) for name in names])
print(max(names, key=lambda n: len(n)))  # first occurance


songs = [{"title": "song1", "playcount": 1},
         {"title": "song2", "playcount": 6},
         {"title": "song3", "playcount": 99},
         {"title": "song4", "playcount": 31}, ]
print("\nleast played song")
print(min(songs, key=lambda s: s['playcount'])
      ['title'])  # least number of playcount
print(max(songs, key=lambda s: s['playcount'])
      ['title'])  # most number of playcount
