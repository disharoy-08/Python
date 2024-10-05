# with open('weather-data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather-data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].max())

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Creating a dataframe from scratch

# data_set = {
#     "students": ["Any", "Janes", "Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_set)
# data.to_csv("new_data.csv")
# print(data)


# New Project

import pandas

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count,black_squirrels_count ]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



