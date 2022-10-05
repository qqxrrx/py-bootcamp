print("\nDictionary Comprehension")
num = dict(first=1, second=2, third=3)
print(f"given dictionary: {num}")
squared_num = {key: value ** 2 for key, value in num.items()}
print(f"squared dictionary: {squared_num}")


print("\n")
print({num: num**2 for num in [1, 2, 3, 4, 5]})


print("\n")
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)


print("\nconditional on key")
person = dict(name="john doe", city="tokyo", color="black")
print({(k.upper() if k is 'color' else k): v.upper()
      for k, v in person.items()})


print("\nconditional on value")
num_list = range(1, 5)
print({num: ("even" if num % 2 == 0 else "odd") for num in num_list})
