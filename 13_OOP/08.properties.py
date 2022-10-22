class Human:
    # we should not access _<variable> by convention (can still access it, but should not be accessed)

    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age

    @property  # getter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be a negative")

    @property
    def fullname(self):
        return f"{self._first} {self._last}"

    def __repr__(self):
        return f"{self.fullname}, {self.age} years old"


jd = Human("john", "doe", 18)
print(jd.age)
jd.age = 16
print(jd.age)
print(jd.fullname)
print(jd)
