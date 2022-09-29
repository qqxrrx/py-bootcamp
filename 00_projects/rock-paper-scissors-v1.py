# -- v1 --

# try to emulate constants in other languages
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
p2 = input(f"(enter {p2s}'s choice): ").lower().strip()

print("SHOOT!")

# rock > scissors
# scissors > paper
# paper > rock
# rock == rock
# paper == paper
# scissors = scissors

if p1 == i.ROCK and p2 == i.SCISSORS:
    print(f"{p1s} win")
elif p1 == i.ROCK and p2 == i.PAPER:
    print(f"{p2s} win")
elif p1 == i.PAPER and p2 == i.ROCK:
    print(f"{p1s} win")
elif p1 == i.PAPER and p2 == i.SCISSORS:
    print(f"{p2s} win")
elif p1 == i.SCISSORS and p2 == i.ROCK:
    print(f"{p2s} win")
elif p1 == i.SCISSORS and p2 == i.PAPER:
    print(f"{p1s} win")
elif p1 == p2:
    print("tie!")
else:
    print("error")
