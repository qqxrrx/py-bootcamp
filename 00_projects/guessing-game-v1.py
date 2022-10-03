# -- v1 --
import random

# .randint() is inclusive, based on argument generate random number between 1 and 10
random_number = random.randint(1, 10)
guess = None

while guess != random_number:
    guess = int(input("Pick a number from 1 to 10: "))

    if guess < random_number:
        print("too low")
    elif guess > random_number:
        print("too high")
    else:
        print(f"{guess} is correct!")
