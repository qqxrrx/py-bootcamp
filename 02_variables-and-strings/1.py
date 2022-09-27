num_of_cats = 0
print(num_of_cats)


num_of_cats = "j"
print(num_of_cats)


a, b, c = 1, 2, 3
print(a, b, c)


myVariable = None
print(myVariable)
print(type(myVariable))


myVariable = "this is the new value"
print(myVariable)
print(type(myVariable))


print("so 'that' was there")
print('we found the "thing"')


print("this is\n another line, after a \t tab")
print("so we have this weird string"
      "and another wierd string")
print("\"what?\"")
print('\'okey\'')


print("this is the" + " <moment>")

try:
    print("we are trying to concatinate like JavaScript!" + 42)
except TypeError as e:
    print("WARNING: " + str(e))

print("wow that does not work, only applies to two strings " + "42")

str_food = "ice"
str_food += " cream"
print(str_food)


a = 2022
print(f"the year today is {a}")
print(f"{2+2} = 2 + 2")
