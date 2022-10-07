def display_name(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}= {v}")


colors = {"first": "red", "second": "blue", "third": "black"}

# dictionary unpacking; called_function(**<argument>)
display_name(**colors)

names = dict(john="doe", pepe="frog", agent="smith")

# can pass extra argument on last position
display_name(**names, extra_arg="meow")
