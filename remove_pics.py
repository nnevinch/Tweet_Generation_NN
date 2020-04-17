import csv
import sys 
  
file_in = sys.argv[1] # name of raw data file
file_out = sys.argv[2] # name of cleaned data file

reader = csv.reader(open(file_in))

with open(file_out,'w') as f_out:
	for row in reader:
		if 'pic.twitter.com' not in row[6] and len(row[6]) > 35:
			csv.writer(f_out).writerow(row)