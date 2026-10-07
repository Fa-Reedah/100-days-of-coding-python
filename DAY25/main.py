# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if int(row[1]) != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
#
# summ = 0
# for i in range(len(data_list)):
#     new_sum = summ + data_list[i]
#     summ = new_sum
# Average = summ/len(data_list)
# print(Average)
#
# print(sum(data_list) / len(data_list))
#
# print( data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data["condition"])
#
# print(data.condition)
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]


print(monday.temp * 9 / 5 + 32)