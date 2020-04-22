import csv
import sys 
  
name = sys.argv[1]
file_in = name + '_updatedheader.csv'
file_out = name + '_picsremoved.csv'

reader = csv.reader(open(file_in))

with open(file_out,'w') as f_out:
	for row in reader:
		if 'pic.twitter.com' not in row[6] or len(row[6]) > 35:
			csv.writer(f_out).writerow(row)