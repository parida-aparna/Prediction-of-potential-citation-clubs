#This program visits each row in the 'sorted_weighted_network.txt' iteratively and counts the number of inside and outside journal citations.
#sys.argv[1]--> folder path of journal
#Input: sorted_weighted_network.txt(file contains the weighted citation links with 'inside' or 'outside' labels) 

import sys

with open(sys.argv[1]+"/sorted_weighted_network.txt",mode='r') as f:
	inside=0
	outside=0
	for row in f:
		row=row.split()
		
		if row[3] == "inside":
			inside=inside+1
		if row[3] == "outside":
			outside=outside+1
	print(f'inside:{inside}\n')	
	print(f'outside:{outside}\n')
