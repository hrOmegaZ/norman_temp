import csv
with open("Norman2016.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row['MONTH'] + '/' + row['DAY'] + '/' + row['YEAR'] + ', TMAX = ' + row["TMAX"] + ', TMIN = ' + row["TMIN"])