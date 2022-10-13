# __repr__
#     allow you to define the representation of an instance if converted to string
#     instead of showing the memory address of a class, we return a custom value

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # instead of <__main__.User object at 0x########>, we return this
        return f"{self.name} is the representation of this instance"


user1 = User("test")
print(user1)
