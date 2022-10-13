class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("john", "doe", 45)
user2 = User("alyssa", "smith", 18)
print(f"{user1.first} {user1.last}, {user1.age} years old")
print(f"{user2.first} {user2.last}, {user2.age} years old")
