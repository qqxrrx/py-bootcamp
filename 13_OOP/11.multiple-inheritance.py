class Aquatic:
    def __init__(self, name):
        print("-- aquatic init --")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        print("-- ambulatory init --")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("-- penguin init --")
        # this will only call the 1st encountered greet()
        # super().__init__(name=name)

        # this can be used to initiate both parents
        # still can't execute greet() on Aquatic
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)


p = Penguin("wow")

print(p.swim())
print(p.walk())

# will only call the 1st class that encounters this function if there are duplicates on next parents
print(p.greet())

print(f"isinstance(p, Aquatic): {isinstance(p, Aquatic)}")
print(f"isinstance(p, Ambulatory): {isinstance(p, Ambulatory)}")
print(f"isinstance(p, Penguin): {isinstance(p, Penguin)}")
print(f"isinstance(p, object): {isinstance(p, object)}")
