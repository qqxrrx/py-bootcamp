import pyfiglet as pf
from termcolor import colored as cl

# help(pyfiglet.figlet_format)


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "magenta"

    ascii_art = pf.figlet_format(msg)
    colored_ascii = cl(ascii_art, color=color)

    print(colored_ascii)


msg = input("what to print?: ")
color = input("what color?: ")

print_art(msg, color)
