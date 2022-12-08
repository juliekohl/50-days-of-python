from typing import Union, Any, List


# Function with outputs
# def format_name(f_name: str, l_name: str) -> str:
#     formatted_f_name: str = f_name.title()
#     formatted_l_name: str = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#
#
# print(format_name("JuLiE", "KoHl"))

# Multiple return values
# def format_name(f_name: str, l_name: str) -> str:
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#
#     formatted_f_name: str = f_name.title()
#     formatted_l_name: str = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"
#
#
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Exercise Days in Month
# def is_leap(year: int) -> bool:
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year: int, month: int) -> Union[Union[str, int], Any]:
#     month_days: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month > 12 or month < 1:
#         return "Invalid month entered."
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month - 1]
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Quiz
# 1
# def add(n1: float, n2: float) -> float:
#     return n1 + n2
#
#
# def subtract(n1: float, n2: float) -> float:
#     return n1 - n2
#
#
# def multiply(n1: float, n2: float) -> float:
#     return n1 * n2
#
#
# def divide(n1: float, n2: float) -> float:
#     return n1 / n2
#
#
# print(add(2, multiply(5, divide(8, 4)))) # 12.0

# 2
# def outer_function(a: int, b: int) -> int:
#     def inner_function(c: int, d: int) -> int:
#         return c + d
#
#     return inner_function(a, b)
#
#
# result = outer_function(5, 10)
# print(result) # 15

# 3
# def my_function(a: int) -> Any:
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
#
#
# print(my_function(25)) # None

# Docstrings
# Multiple lines of comments
