# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print("data", data)
#     for row in data:
#         # print("row", row)
#         # print("row[1]", row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# Pandas
# import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print("Dict", data_dict)

# temp_list = data["temp"].to_list()
# print("List", temp_list)
# print("List len", len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print("average", average)
# print("mean()", data["temp"].mean())
# print("max", data["temp"].max())

# Get Data in Columns
# print(data["condiction"]) # use like dict
# print(data.condiction) # use like objs

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a datafreame from screatch
# data_dict = {
#     "studants": ["Julie", "Angie", "Kelly"],
#     "scores": [87, 85, 88],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new-data.csv") # this will create new file with the data_dict inside!

# Squirrel Count csv
# data = pandas.read_csv("2018-central-park-squirrel-census-squirrel-data.csv")
# grey_squirrels_count: float = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count: float = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count: float = len(data[data["Primary Fur Color"] == "Black"])
#
# print(grey_squirrels_count) # 2473
# print(red_squirrels_count) # 392
# print(black_squirrels_count) # 103
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
# }
#
# dataframe = pandas.DataFrame(data_dict)
# dataframe.to_csv("squirrel_count.csv")

# U.S States Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x: float, y: float) -> None:
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor) # get coord like this 139,-77
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

