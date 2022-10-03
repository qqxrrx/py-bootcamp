# -- v3 --
from random import randint


class RPS_Answers(object):
    # try to emulate constants in other languages
    # prevent mistyped choices on code
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def __setattr__(self, *_):
        pass


i = RPS_Answers()

print(f"...{i.ROCK}...\n...{i.PAPER}...\n...{i.SCISSORS}...")

p1s = "player"
p2s = "computer"
p1 = input(f"(enter {p1s}'s choice): ").lower().strip()


# computer play
p2 = ""
rand_num = randint(0, 2)
if rand_num == 0:
    p2 = i.ROCK
elif rand_num == 1:
    p2 = i.PAPER
else:
    p2 = i.SCISSORS

print(f"({p2s}'s choice): {p2}")

print("SHOOT!")

# rock > scissors
# scissors > paper
# paper > rock
# rock == rock
# paper == paper
# scissors == scissors

# refactor 1: towards if-elif nesting
# refactor 2: because computer can only choose in one of 3 moves, then eliminate the last 'elif' check and make it 'else'
if p1 == p2:  # shortcircuit to prevent evaluating others
    print("tie!")
elif p1 == i.ROCK:
    if p2 == i.SCISSORS:
        print(f"{p1s} wins!")
    else:
        print(f"{p2s} wins!")
elif p1 == i.PAPER:
    if p2 == i.ROCK:
        print(f"{p1s} wins!")
    else:
        print(f"{p2s} wins!")
elif p1 == i.SCISSORS:
    if p2 == i.PAPER:
        print(f"{p1s} wins!")
    else:
        print(f"{p2s} wins!")
else:
    print(
        f"enter a valid move between: \"{i.ROCK}\", \"{i.PAPER}\", \"{i.SCISSORS}\"")
