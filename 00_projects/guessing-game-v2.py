import random

# .randint() is inclusive, based on argument generate random number between 1 and 10
random_number = random.randint(1, 10)
guess = None

while True:
    guess = int(input("Pick a number from 1 to 10: "))

    if guess < random_number:
        print("too low")
    elif guess > random_number:
        print("too high")
    else:
        print(f"{guess} is correct!")
        play_again = input("want to play again? (y/n): ")
        if play_again == 'y':
            random_number = random.randint(1, 10)
            guess = None
            print("\n\n\n")
        else:
            print("quitting game...")
            break
