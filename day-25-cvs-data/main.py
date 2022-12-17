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
import pandas

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
