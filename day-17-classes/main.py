# Classes
from typing import Any


class User:

    def __int__(self, id: int = 0, username: str = "") -> None:
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user) -> None:
        user.followers += 1
        self.following += 1



user_1 = User(001, "Julie")
user_2 = User(002, "César")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
