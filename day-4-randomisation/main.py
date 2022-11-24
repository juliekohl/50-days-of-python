# import random
# Random Modules
#
# randomIntegeter = random.randint(1, 10)
# print(randomIntegeter)
#
# randomFloat = random.random() * 5
# print(randomFloat)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
import random

# Exercise Heads or Tails
# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("Heads")
# else:
#   print("Tails")

# Offset and appending items to lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# print(states_of_america)
# print(states_of_america[3]) # Georgia
#
# states_of_america[3] = "Georgya"
# print(states_of_america[3]) # Georgya
#
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# "Tomatoes", "Celery", "Potatoes"]
#
# states_of_america.extend(dirty_dozen)
# print(states_of_america)

# Exercise Banker Roulette
# import random
#
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# # Get the total number of items in list.
# num_items = len(names)
# # Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# # Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]
#
# print(person_who_will_pay + " is going to buy the meal today!")

# Index Errors and Nested lists

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits[-5]) # Apples
# fruits[-1] = "Melons" # remove -1 and add "Melons"
# fruits.append("Lemons") # add "Lemons"
# print(fruits) # remove "Pears" and add "Melons" and "Lemons"

# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# print(fruits[6]) # Pears
# # print(fruits[7]) # error
#
# len_fruits = len(fruits)
# print(len_fruits) # 7
# # print(fruits[len_fruits]) # error
# print(fruits[len_fruits - 1]) # Pears
#
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][1]) # "Kale"
# print(dirty_dozen[0]) # fruits only
# print(dirty_dozen[1]) # vegetables only
# print(dirty_dozen[1][2]) # Tomatoes
# print(dirty_dozen[1][3]) # Celery

# Treasure Map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure? ")
#
# row = int(position[0])
# col = int(position[1])
#
# map[col - 1][row - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

# Project 4 - Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
  