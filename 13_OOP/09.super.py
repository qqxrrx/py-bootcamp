class Animal:
    cool = True

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f'this animal says "{sound}"')


class Cat(Animal):
    def __init__(self, name, breed, toy):
        # Animal.__init__(self, name, species)
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


c = Cat("C1", "tabby", "bone")
print(c)
print(c.name)
print(c.species)
print(c.breed)
print(c.toy)
c.play()
