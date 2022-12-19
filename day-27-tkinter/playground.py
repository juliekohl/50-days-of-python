# *args
# def add(*args: int) -> int:
#     # print(type(args)) # class 'tuple'
#     # print(args[0]) # 3
#     # print(args[1]) # 5
#     sum: int = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3, 5, 6, 2, 1, 7, 4, 3)) # 31

from typing import Dict, Any


# **kwargs
# def calculate(n: int, **kwargs: Dict[str, Any]) -> None:
#     # print(type(kwargs)) # class 'dict'
#     print(kwargs) # {'add': 3, 'multiply': 5}
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n) # 25
#
#
# calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw: Dict[str, str]) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.make)
print(my_car.color)

