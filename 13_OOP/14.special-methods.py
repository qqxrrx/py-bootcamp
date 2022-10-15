# also called magic methods

from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="baby", last=self.last, age=0)
        raise TypeError("should be a valid human")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError("should be a valid number")


jd = Human("John", "Doe", 77)
kj = Human("Kate", "Jones", 18)
print(jd)
print(len(jd))
print(jd+kj)
print(jd*2)
