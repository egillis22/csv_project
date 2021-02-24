import csv
from datetime import datetime

open_valley = open("death_valley_2018_simple.csv", "r")
open_sitka = open("sitka_weather_2018_simple.csv", "r")

valley_file = csv.reader(open_valley, delimiter=",")
sitka_file = csv.reader(open_sitka, delimiter=",")

header_row_valley = next(valley_file)
header_row_sitka = next(sitka_file)

valleyindexes = {}
sitkaindexes = {}

for index, column_header in enumerate(header_row_valley):
    valleyindexes[column_header] = index
for index, column_header in enumerate(header_row_sitka):
    sitkaindexes[column_header] = index

valleyhighs = []
valleylows = []
valleydates = []
valleyname = ""
for row in valley_file:
    try:
        high = int(row[valleyindexes["TMAX"]])
        low = int(row[valleyindexes["TMIN"]])
        converted_date = datetime.strptime(row[valleyindexes["DATE"]], "%Y-%m-%d")
        valleydates.append(converted_date)
        valleyname = str(row[valleyindexes["NAME"]])
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        valleyhighs.append(high)
        valleylows.append(low)


sitkahighs = []
sitkalows = []
sitkadates = []
sitkaname = ""
for row in sitka_file:
    sitkahighs.append(int(row[sitkaindexes["TMAX"]]))
    converted_date = datetime.strptime(row[sitkaindexes["DATE"]], "%Y-%m-%d")
    sitkadates.append(converted_date)
    sitkalows.append(int(row[sitkaindexes["TMIN"]]))
    sitkaname = str(row[sitkaindexes["NAME"]])
import matplotlib.pyplot as plt


fig2, a = plt.subplots(2)
fig2.suptitle(
    f"Temperature comparison between {sitkaname} and {valleyname}", fontsize=12
)
a[0].plot(valleydates, valleyhighs, c="red")
a[0].plot(valleydates, valleylows, c="blue")
a[0].fill_between(valleydates, valleyhighs, valleylows, facecolor="blue", alpha=0.1)
a[0].set_title(valleyname, fontsize=12)
a[0].tick_params(labelbottom=False)

a[1].plot(sitkadates, sitkahighs, c="red")
a[1].plot(sitkadates, sitkalows, c="blue")
a[1].fill_between(sitkadates, sitkahighs, sitkalows, facecolor="blue", alpha=0.1)
a[1].set_title(sitkaname, fontsize=12)
plt.show()
