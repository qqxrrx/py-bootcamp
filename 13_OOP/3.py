class User:
    active_users = 0

    # class method
    @classmethod
    def display_active_users(cls):
        # cls = class and not instance (self)
        return f"There are {cls.active_users} active users"

    def __init__(self, name):
        self.name = name
        User.active_users += 1

    def logout(self):
        User.active_users -= 1


user1 = User("A")
user2 = User("B")
print(User.display_active_users())

user3 = User("C")
user4 = User("D")
print(User.display_active_users())
