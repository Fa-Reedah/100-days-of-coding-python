import pandas
 
data = pandas.read_csv("squirrel_archive.csv")

color = data["Primary Fur Color"]

black_count = len(data[color == "Black"])
gray_count = len(data[color == "Gray"])
red_count = len(data[color == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count":[black_count, gray_count, red_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel.csv")
print(df)
