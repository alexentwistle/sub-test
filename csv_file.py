import csv

infilename = r'discovered.csv'
outfilename = r'processed.csv'


with open(infilename, 'r') as fp_in, open(outfilename, 'w') as fp_out:
	reader = csv.reader(fp_in)
	writer = csv.writer(fp_out)
	# header = "URL"
	# writer.writerow(header)
	for row in reader:
		chars = ["'" , "[" , "]"]
		for c in chars: 
			new_row = str(row).replace(c,"")
	#	new_row = 'https://' + str(row)
		writer.writerow([new_row])

	#for row in reader:
   	#	print(row[0])