import csv
import sys

file_in = sys.argv[1] # name of initial data file
file_out = sys.argv[2] # name of cleaned data file

reader = csv.reader(open(file_in))

with open(file_out,'w') as f_out:
	for row in reader:
		copy = row

		if len(row[6]) < 280:
			toAdd = ''
			for i in range(0, 280 - len(row[6])):
				toAdd = toAdd + ' '
			copy[6] = toAdd + copy[6]

		csv.writer(f_out).writerow(copy)
