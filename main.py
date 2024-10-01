
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_color = data["Primary Fur Color"]
# print(squirrel_color)
color_counts = data['Primary Fur Color'].value_counts()
print(color_counts)