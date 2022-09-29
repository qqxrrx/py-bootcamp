city = input("where do you live?: ").lower().strip()

if city == "los angeles" or city == "san francisco":
    print(f"you live in \"{city}\"")
else:
    print("you live somewhere else")
