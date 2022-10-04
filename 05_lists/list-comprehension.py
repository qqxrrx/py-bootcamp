nums = [1, 2, 3]
print(nums)
# for every x in num multiply it by 10 and put on a new list
print([x*10 for x in nums])


nums = [1, 2, 3, 4, 5]
print(nums)
print([num*2 for num in nums])


phrase = "peter pipper picked a peck of pickled pepper"
print(phrase)
print([c.upper() for c in phrase])


people = ["ben", "maria", "roy"]
print(people)
print([person[0].upper()+person[1:] for person in people])


print([num*10 for num in range(1, 6)])
print([bool(val) for val in [0, [], '']])


nums = [1, 2, 3, 4, 5]
print(nums)
print([str(num) for num in nums])


print("conditional list comprehension")
numbers = [1, 2, 3, 4, 5]
print(f"odds: {[num for num in numbers if num % 2 != 0]}")
print(f"evens: {[num for num in numbers if num % 2 == 0]}")


# more complex example:
#   if num has no remainder, multiply num by 2
#   else divide num by 2
print([num*2 if num % 2 == 0 else num/2 for num in numbers])


# combination with "in"
# .join() list into a string
with_vowels = "The quick brown fox jumped over the lazy dog"
print(''.join([char for char in with_vowels if char not in "aeiou"]))
