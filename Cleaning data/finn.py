
import csv

makes = []
with open('kjopes_finn.csv', 'r') as f:
    reader = csv.reader(f)
    #next(reader) # Ignore first row

    for row in reader:
        makes.append(row[0])
        print(row[0])

