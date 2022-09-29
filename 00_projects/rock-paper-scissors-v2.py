# try to emulate constants in other languages
# prevent mistyped choices on code
class RPS_Answers(object):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def __setattr__(self, *_):
        pass


i = RPS_Answers()
print(f"...{i.ROCK}...\n...{i.PAPER}...\n...{i.SCISSORS}...")

p1s = "player 1"
p2s = "player 2"
p1 = input(f"(enter {p1s}'s choice): ").lower().strip()
print("***NO CHEATING!\n\n"*20)
p2 = input(f"(enter {p2s}'s choice): ").lower().strip()

print("SHOOT!")

# rock > scissors
# scissors > paper
# paper > rock
# rock == rock
# paper == paper
# scissors = scissors

# refactor towards if-elif nesting
if p1 == p2:  # shortcircuit to prevent evaluating others
    print("tie!")
elif p1 == i.ROCK:
    if p2 == i.SCISSORS:
        print(f"{p1s} wins!")
    elif p2 == i.PAPER:
        print(f"{p2s} wins!")
elif p1 == i.PAPER:
    if p2 == i.ROCK:
        print(f"{p1s} wins!")
    elif p2 == i.SCISSORS:
        print(f"{p2s} wins!")
elif p1 == i.SCISSORS:
    if p2 == i.PAPER:
        print(f"{p1s} wins!")
    elif p2 == i.ROCK:
        print(f"{p2s} wins!")
else:
    print("error")
