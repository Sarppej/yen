import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240522.csv")
#
gray_squirrel_count= len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count= len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count= len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray","Black","Red"],
    "Count" : [gray_squirrel_count,black_squirrel_count,red_squirrel_count]
}
print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)