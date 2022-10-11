import requests as rq
from random import choice
from pyfiglet import figlet_format as ff
from termcolor import colored as cl

header = ff("DAD JOKES!")
header = cl(header, color="magenta")
print(header)

input = input("What do you want to search?: ")
url = "https://icanhazdadjoke.com/search"

rs = rq.get(
    url,
    headers={"Accept": "application/json"},
    params={
        "term": input
    }).json()

num_jokes = rs['total_jokes']
results = rs['results']

if num_jokes == 0:
    print("no joke found")
else:
    print(f"found {num_jokes} about {input}:")

    if num_jokes > 1:
        print(choice(results)['joke'])
    else:
        print(results[0]['joke'])
