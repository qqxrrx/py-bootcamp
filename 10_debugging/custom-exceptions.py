# once you 'raise' an error, it will terminate execution
#
#   raise ValueError('invalid value')
#   raise NameError('bad name')


def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be a string")

    if type(color) is not str:
        raise TypeError("color must be a string")

    colors = ("cyan", "yellow", "blue", "green", "magenta")

    if color not in colors:
        raise ValueError("input a valid color")

    print(f"{text} in {color}")


colorize("hey", "cyan")
