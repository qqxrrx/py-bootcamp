class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        name, id = data_str.split(',')
        return cls(name, int(id))

    def __init__(self, first, last, age):
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


class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are {cls.total_mods} active mods"

    def remove_post(self):
        print(
            f"{self.full_name()} has removed a post from the {self.community} community.")


user1 = User("john", "doe", 65)
print(User.display_active_users())

user2 = User("alyssa", "smith", 18)
print(User.display_active_users())

print(f"{user1.likes('fresh cookies')}")
print(f"{user2.likes('warm milk')}")

print(f"{user1.initials()} {user1.birthday()} -- senior? {user1.is_senior()}")
print(f"{user2.initials()} {user2.birthday()} -- senior? {user2.is_senior()}")

user1.say_hi()
user2.say_hi()

user1.logout()
print(User.display_active_users())
user2.logout()
print(User.display_active_users())

newmod1 = Moderator("sam", "sam", 1, "saxophone")
print(User.display_active_users())
print(newmod1.full_name())
print(newmod1.community)


user3 = User("Maria", "Maria", 14)
print(User.display_active_users())
user4 = User("Shia", "Shia", 16)
print(User.display_active_users())
print(Moderator.display_active_mods())
newmod2 = Moderator("sem", "sem", 1, "bass")
print(Moderator.display_active_mods())
