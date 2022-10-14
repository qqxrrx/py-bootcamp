# same class method works in similar way for different classes:

class Animal():
    def speak(self):
        raise NotImplementedError("subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())
f = Fish()
# print(f.speak()) # will throw an error

# -----------------------------------------------------------------


# same operation works for different kinds of objects

print(8+2)  # int addition
print("8" + "2")  # string concatenation

# using builtin methods:
print(len("abcdef"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))

# -----------------------------------------------------------------
