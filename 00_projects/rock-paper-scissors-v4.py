# -- v4 --
from random import randint


class RPS_Answers(object):
    # try to emulate constants in other languages
    # prevent mistyped choices on code
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    WINNING_SCORE = 2

    def __setattr__(self, *_):
        pass


i = RPS_Answers()

player_wins = 0
computer_wins = 0
p1s = "player"
p2s = "computer"

while player_wins < i.WINNING_SCORE and computer_wins < i.WINNING_SCORE:

    print(f"player score: {player_wins}\ncomputer score: {computer_wins}")
    print(f"...{i.ROCK}...\n...{i.PAPER}...\n...{i.SCISSORS}...")

    print("NOTE: enter 'quit' or 'q' to quit")

    p1 = input(
        f"(enter {p1s}'s choice): ").lower().strip()

    if p1 == 'quit' or p1 == 'q':
        break

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
        print("tie!\n")
    elif p1 == i.ROCK:
        if p2 == i.SCISSORS:
            print(f"{p1s} scores!\n")
            player_wins += 1
        else:
            print(f"{p2s} scores!\n")
            computer_wins += 1
    elif p1 == i.PAPER:
        if p2 == i.ROCK:
            print(f"{p1s} scores!\n")
            player_wins += 1
        else:
            print(f"{p2s} scores!\n")
            computer_wins += 1
    elif p1 == i.SCISSORS:
        if p2 == i.PAPER:
            print(f"{p1s} scores!\n")
            player_wins += 1
        else:
            print(f"{p2s} scores!\n")
            computer_wins += 1
    else:
        print(
            f"enter a valid move between: \"{i.ROCK}\", \"{i.PAPER}\", \"{i.SCISSORS}\"")

print(f"final scores:")
print(f"player: {player_wins}\ncomputer: {computer_wins}\n")

if player_wins > computer_wins:
    print(f"{p1s} won")
elif player_wins == computer_wins:
    # only happens if has both score before round ends and player suddenly quits
    print("tie!")
else:
    print(f"{p2s} won")
