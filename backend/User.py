class User:

    def __init__(self, username, password, age):
        if age < 0:
            raise ValueError("Age cannot be negative")

        self.username = username
        self.password = password
        self.age = age
        self.points = 0

    def addPoints(self, pointNum):
        self.points += pointNum