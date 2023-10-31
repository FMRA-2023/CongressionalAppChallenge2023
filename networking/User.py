import bcrypt
import os
import uuid

class User:
    def __init__(self, username, password, age):
        if age < 0:
            raise ValueError("Age cannot be negative")

        self.salt = bcrypt.gensalt() 
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), self.salt)

        self.username = username 
        self.age = age
        self.points = 0
        self.events_signed_up = []
        self.id = str(uuid.uuid4())

    def addPoints(self, pointNum):
        self.points += pointNum

    def verify_password(self, entered_password):
        hashed_entered_pw = bcrypt.hashpw(entered_password.encode('utf-8'), self.salt)
        print(hashed_entered_pw)
        print(self.hashed_password)
        if hashed_entered_pw == self.hashed_password:
            return True
        else:
            return False
    
    def sign_up_event(self, event):
        if self.age < event.minimumAge or self.age > event.maximumAge:
            print("User age does not meet requirements for this event")
            return
        print(f"{self.username} signed up for {event.name}")
        self.addPoints(10)
        self.events_signed_up.append(event)
        event.signups.append(self.id)



user = User('john', 'password123', 25)

if user.verify_password('password123'):
  print("Password verified")
else:
  print("Wrong password")
