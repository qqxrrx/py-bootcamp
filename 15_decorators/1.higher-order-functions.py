# high order function example

from random import choice


# return value
def greet(person):
    def get_mood():
        msg = choice(('hey', 'go away', 'wow'))
        return msg

    return f'"{get_mood()}" {person}'


print(greet("john doe"))


# return function
def make_laugh_func():
    def get_laugh():
        return choice(("kek", 'kuku', 'hehe'))
    return get_laugh


laugh = make_laugh_func()
print(laugh())


# use function from argument
def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x**2


def cube(x):
    return x**3


print(sum(10, square))
print(sum(10, cube))
