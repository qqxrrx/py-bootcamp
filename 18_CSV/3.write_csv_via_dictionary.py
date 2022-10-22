from csv import DictReader, DictWriter

# with open("example.csv", mode="w") as f:
#     headers = ['Character', 'Move']
#     csv_writer = DictWriter(f, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Character": "Ryu",
#         "Move": "Hadouken"
#     })

# with open("cats.csv", mode="w") as f:
#     headers = ['Name', 'Breed', 'Age']
#     csv_writer = DictWriter(f, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Name": "Garfield",
#         "Breed": "Orange Tabby",
#         "Age": "99"
#     })


# reading and writing:
with open("fighters.csv") as original_file:
    csv_reader = DictReader(original_file)
    with open('inches_fighters.csv', mode="w") as new_file:
        headers = ['Name', 'Country', 'Height (in inches)']
        csv_writer = DictWriter(new_file, fieldnames=headers)
        csv_writer.writeheader()
        for fighter in csv_reader:
            csv_writer.writerow({
                "Name": fighter['Name'],
                "Country": fighter['Country'],
                "Height (in inches)": float(fighter['Height (in cm)']) * 0.393701
            })
