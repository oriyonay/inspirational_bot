# small script to process quotes from CSV file
import csv

QUOTES_IN = 'quotes.csv'
QUOTES_OUT = 'quotes.txt'

f = open(QUOTES_OUT, 'w')
with open(QUOTES_IN, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if len(row[0]):
            f.write('"' + row[1] + '" -' + row[0] + '\n')

f.close()
