# Namespaces Local vs. Global Scope
from typing import List

# Scope
# enemies: int = 1
#
# def increase_enemies() -> None:
#   enemies = 2
#   print(f"enemies inside function: {enemies}") # 2
#
# increase_enemies()
# print(f"enemies outside function: {enemies}") # 1

# Local Scope
# def drink_potion() -> None:
#     potion_strength: int = 2
#     print(potion_strength) # 2
#
# drink_potion()
# print(potion_strength) Error var is not defined

# Global Scope
# player_health: int = 10
#
# def drink_potion() -> None:
#     potion_strength: int = 2
#     print(player_health) # 10
#
# drink_potion()
# print(player_health) # 10

# There is no Block Scope
# game_level: int = 3
#
#
# def create_enemy() -> None:
#     enemies: List[str] = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy: str = enemies[0]
#
#     print(new_enemy)


# print(new_enemy) # error var is not defined

# Modify a Global Variable
# enemies: int = 1
#
#
# def increase_enemies() -> int:
#     print(f"enemies inside function: {enemies}")  # 1
#     return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")  # 2

# Constants & Global Scope
# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@julianaCochenski"

# Quiz
# 1
# def a_function(a_parameter: int) -> int:
#     a_variable: int = 15
#     return a_parameter
#
#
# a_function(10)
# print(a_variable) # error Name Error

# 2
# i: int = 50
#
#
# def foo() -> int:
#     i = 100
#     return i
#
#
# foo()
# print(i) # 50

# 3
# def bar() -> None:
#     my_variable: int = 9
#
#
# if 16 > 9:
#     my_variable = 16
#
# print(my_variable) # 16
#
# bar()

# Project - Number Guessing Game
from random import randint
from art import logo

EASY_LEVEL_TURNS: int = 10
HARD_LEVEL_TURNS: int = 5


def check_answer(guess: int, answer: int, turns: int) -> int:
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return answer


def set_difficulty() -> int:
    level: str = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game() -> None:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer: int = randint(1, 100)
    # print(f"Pssst, the correct answer is {answer}")

    turns: int = set_difficulty()
    guess: int = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
