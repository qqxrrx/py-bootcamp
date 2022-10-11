print({x**2 for x in range(10)})

print({char.upper() for char in 'aaabbbcccdddeefffggghhhhiiijj'})


def are_all_vowels_in_string(str):
    return len({char for char in str if char in 'aeiou'}) == 5


print(are_all_vowels_in_string("the quick brown fox jumped over the lazy dog"))
print(are_all_vowels_in_string("peter pipper picked a peck of pickled pepper"))
