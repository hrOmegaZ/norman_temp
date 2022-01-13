import csv
Avg_Max = []
Avg_Min = []
TMIN = 200
TMAX = 0
with open("Norman2016.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if float(row['TMAX']) > 200 or float(row['TMAX']) < -200:
            pass
        else:
            Avg_Max.append(float(row["TMAX"]))
            if float(row['TMAX']) > TMAX:
                TMAX = float(row['TMAX'])
        if float(row['TMIN']) > 200 or float(row['TMIN']) < -200:
            pass
        else:
            Avg_Min.append(float(row["TMIN"]))
            if float(row['TMIN']) < TMIN:
                TMIN = float(row['TMIN'])
    Avg_MaxTemp = round(sum(Avg_Max)/len(Avg_Max) + 1, 2)
    Avg_MinTemp = round(sum(Avg_Min)/len(Avg_Min) + 1, 2)
    print(Avg_Max)
    print(Avg_Min)
    print(f'Max Temp = {TMAX}, Min Temp = {TMIN}')
    print(f'Avg. Max = {Avg_MaxTemp}, Avg. Min = {Avg_MinTemp}')

'''months = ['January','February','March','April','May','June','July','August','September','October','November','December']'''
'''print(months[int(row['MONTH']) - 1] + ' ' + row['DAY'] + ', ' + row['YEAR'] + '; TMAX = ' + row["TMAX"] + ', TMIN = ' + row["TMIN"])'''
# Max temp = 100.47, Min Temp = 4.28
# Avg. Max = 74.14, Avg. Min = 52.34