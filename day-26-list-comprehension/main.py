from typing import List

import pandas

# List Comprehension
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
student_dict = {
    "students": ["Julie", "Angie", "Kelly"],
    "scores": [87, 85, 88],
}

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

