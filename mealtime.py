import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def mealtime_identification(file):
    meal_size = list()
    parsed_meal_size = list()
    temp_count = 0

    with open(file, 'r') as data:
        csv_reader = csv.reader(data)
        temp_str = "1990-1-1 0:0:0"
        for index, item in enumerate(csv_reader):

            if len(item) >= 41 and item[24] != "BolusType":
                if item[24] != "Carb":


                    date_time_obj = datetime.datetime.strptime(temp_str, '%Y-%m-%d %H:%M:%S')
                    meal_size.append((temp_count, date_time_obj))
                    temp_count = 0
                if item[28] != '0' and item[24] == "Carb":
                    temp_count += float(item[28])
                    temp_str = item[22][0:10] + " " + item[22][11:]

    for i in range(0, len(meal_size)):
        if meal_size[i][0] == 0:
            continue
        if meal_size[i][0] != 0:
            parsed_meal_size.append(meal_size[i])
    return parsed_meal_size
