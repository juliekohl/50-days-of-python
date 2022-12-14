from typing import List

import pandas

# List Comprehension
# For Loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# List Comprehension
# new_list = [n + 1 for n in numbers]

# String as List
# name = "Juliana"
# letters_list = [letter for letter in name]

# Range as List
# range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprenhension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
#
# upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
# import random
# student_grades = {name: random.randint(1, 100) for name in names}
# print(student_grades)
#
# passed_students = {
#     student: grade
#     for (student, grade) in student_grades.items() if grade >= 60
# }
# print(passed_students)


# numbers: List[int] = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers: List[int] = [number * number for number in numbers]
# print(squared_numbers)
#
# result: List[int] = [number for number in numbers if number % 2 == 0]
# print(result)
#
# # Exercise 3
# # with open("file1.txt") as file1:
# #     list1 = file1.readlines()
# #
# # with open("file2.txt") as file2:
# #     list2 = file2.readlines()
# #
# #
# # result: List[int] = [int(number) for number in list1 if number in list2]
# #
# # print(result)
#
# # Refactor U.S. States Game
# import turtle
# import pandas
#
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []
#
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = [state for state in all_states if state not in guessed_states]
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)
#
#

# Dictionary Comprehension
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# student_dict = {
#     "students": ["Julie", "Angie", "Kelly"],
#     "scores": [87, 85, 88],
# }

# Loop through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# import pandas
#
# student_dict_frame = pandas.DataFrame(student_dict)
# print(student_dict_frame)

# Loop through a data frame
# for (key, value) in student_dict_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
# for (index, row) in student_dict_frame.iterrows():
#     # print(row.student)
#     # print(row.score)
#     if row.student == "Juliana":
#         print(row.score)

# NATO Alphabet Project
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
