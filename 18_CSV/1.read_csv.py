from csv import reader, DictReader

print("\nusing reader:")
with open("fighters.csv") as f:
    csv_reader = reader(f)  # give iterator as list
    # reader(f,delimeter="")
    next(csv_reader)  # move next to ignore the headers
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")


print("\nusing DictReader:")
with open("fighters.csv") as f:
    csv_reader = DictReader(f)  # give iterator as ordered Dict
    # DictReader(f,delimeter="")
    for fighter in csv_reader:
        print(f"{fighter['Name']} is from {fighter['Country']}")


# delimiter = if the separator is not ','
