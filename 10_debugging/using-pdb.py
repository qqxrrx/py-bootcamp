import pdb

pdb.set_trace()

first = 1
second = 2
result = first + second
result += result
print(result)

# common pdb commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

# > you can type the variable names to examine it's value
# > imports can be defined inside a function
# > not something you keep in your code
# > commands on pdb will conflict with variable names! so check pdb commands and rename variables accordingly
