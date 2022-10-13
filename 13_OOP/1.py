class User:

    # class attribute that exists across all instances
    active_users = 0

    def __init__(self, first, last, age):
        myvariable = 0  # this is scoped within this block only
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}.".upper()

    def likes(self, thing):
        return f"{self.full_name()} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

    def say_hi(self):
        print("hello")


user1 = User("john", "doe", 65)
print(user1.active_users)
user2 = User("alyssa", "smith", 18)
print(user2.active_users)
print(f"{user1.likes('fresh cookies')}")
print(f"{user2.likes('warm milk')}")

print(f"{user1.initials()} {user1.birthday()} -- senior? {user1.is_senior()}")
print(f"{user2.initials()} {user2.birthday()} -- senior? {user2.is_senior()}")

user1.say_hi()
user2.say_hi()

user1.logout()
print(user1.active_users)
user2.logout()
print(user1.active_users)
