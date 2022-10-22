# import json

# j1 = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# print(j1)


# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed


# c = Cat("Charles", "Tabby")
# j2 = json.dumps(c.__dict__)
# print(j2)

# code above for limited use case, use jsonpickle for encoding and decoding objects into json
# >>> py -m pip install jsonpickle

import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Charles", "Tabby")

with open("cat.json", "w") as f:
    frozen = jsonpickle.encode(c)
    f.write(frozen)


with open("cat.json", "r") as f:
    contents = f.read()
    unfrozen = jsonpickle.decode(contents)  # reconstruct json to python object
    print(unfrozen)
