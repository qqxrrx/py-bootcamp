age = 21
# 2~8, $2
# 65, $5
# else, $10

# this can be refactored into a simplier code
# made this for 'not' logical operator example
if not ((age >= 1 and age <= 8) or (age >= 65)):
    print("$10")
else:
    if (age >= 1 and age <= 8):
        print("$2")
    else:
        print("$5")
