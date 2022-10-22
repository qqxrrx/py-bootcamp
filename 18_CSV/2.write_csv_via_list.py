from csv import reader, writer

# with open("fighters.csv", mode="w") as f:
#     csv_writer = writer(f)
#     csv_writer.writerow(["Character", "Move"])
#     csv_writer.writerow(["Ryu", "Hadouken"])

# with open("cats.csv", mode="w") as f:
#     csv_writer = writer(f)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])


# reading and writing:
with open("fighters.csv") as original_file:
    csv_reader = reader(original_file)
    with open('screaming_fighters.csv', mode="w") as new_file:
        csv_writer = writer(new_file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
