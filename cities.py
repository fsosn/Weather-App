import csv

FILE_PATH = "cities/cities.csv"


def load_city_names():
    city_names = []
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city_names.append(row["name"])
    return city_names
