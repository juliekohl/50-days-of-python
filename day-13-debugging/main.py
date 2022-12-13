# DEBUGGING
# # Describe Problem
# def my_function() -> None:
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()
from typing import List


# # Reproduce the Bug
# from random import randint
# from typing import List
#
# dice_imgs: List[str] = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num: int = randint(1, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year: int = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# age: int = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages: int = 0
# word_per_page: int = 0
# pages: int = int(input("Number of pages: "))
# word_per_page: int = int(input("Number of words per page: "))
# total_words: int = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list: List[int]) -> None:
#     b_list: List[int] = []
#     for item in a_list:
#         print(item * 2)
#         new_item: int = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# Debugging Odd or Even
number: int = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
