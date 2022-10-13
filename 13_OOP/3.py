class User:
    active_users = 0

    # class method
    @classmethod
    def display_active_users(cls):
        # cls = class and not instance (self)
        return f"There are {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        name, id = data_str.split(',')
        return cls(name, int(id))  # new class as the return value

    def __init__(self, name, id):
        self.name = name
        self.id = id
        User.active_users += 1

    def logout(self):
        User.active_users -= 1


user1 = User("A", 1)
user2 = User("B", 2)
print(User.display_active_users())

user3 = User("C", 3)
user4 = User("D", 4)
print(User.display_active_users())

user5 = User.from_string("A,99")
print(User.display_active_users())
