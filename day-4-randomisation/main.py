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
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#
# states_of_america.extend(dirty_dozen)
# print(states_of_america)

# Exercise Banker Roulette
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
