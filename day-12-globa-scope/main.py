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
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@julianaCochenski"
