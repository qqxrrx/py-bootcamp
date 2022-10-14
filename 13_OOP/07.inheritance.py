class Animal:
    cool = True

    def make_sound(self, sound):
        print(f'this animal says "{sound}"')


class Cat(Animal):
    pass


c = Cat()
c.make_sound("meow")
print(c.cool)

print("\ncheck if object is an instance of a class:")
print(f"isinstance(c, Cat): {isinstance(c, Cat)}")
print(f"isinstance(c, Animal): {isinstance(c, Animal)}")
print(f"isinstance(c, object): {isinstance(c, object)}")
