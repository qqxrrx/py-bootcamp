def fullname(first, last):
    return f"you are {first} {last}"


# order does not matter with keyword arguments
# adds flexibility and readability
print(fullname(first='john', last='doe'))
print(fullname(last='doe', first='john'))
