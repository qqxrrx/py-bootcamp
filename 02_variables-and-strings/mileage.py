# mileage converter
# convert kilometers to miles

print("kilometers to convert:")
km = input()
miles = float(km)/1.60934
# .round() = round the decimal value
miles = round(miles, 2)
print(f"that was ({km} Kilometers) or ({miles} Miles)")
