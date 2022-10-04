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
