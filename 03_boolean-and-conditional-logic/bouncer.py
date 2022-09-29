# ask for age
age = input("your age?: ").strip()

# if anything in age, it is truthy
# if empty, it is falsy
if age:

    age = int(age)

    # 18-21 wristband
    # 21+ drink, normal entry
    # too young, sorry

    # if (age >= 18 and age <= 21):
    #     print("can enter, wear wristband")
    # elif (age > 21):
    #     print("can enter and drink")
    # else:
    #     print("too young, access denied")

    # refactor, check from higher value 1st:
    if age >= 21:
        print("can enter and drink")
    elif age >= 18:
        print("can enter, wear wristband")
    else:
        print("too young, access denied")

else:
    print("enter a valid age")
