# import random as r  # <- whole module
from random import randint as r, choice, shuffle  # <- specific part of module

print(choice(["apple", "banana", "cherry", "durian"]))
print(r(1, 100))
print(shuffle(["apple", "banana", "cherry", "durian"]))
