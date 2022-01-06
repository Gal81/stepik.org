import csv

crimes = {}
with open('base\\dump\\Crimes.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if '2015' in row[2]:
            key = row[5]
            if key in crimes:
                crimes[key] += 1
            else:
                crimes[key] = 1

max = 0
maxCrime = ''
for crime in crimes:
    if crimes[crime] > max:
        max = crimes[crime]
        maxCrime = crime

print(maxCrime)