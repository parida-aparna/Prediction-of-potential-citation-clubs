#This program converts the 'sorted_weighted_network.txt' file to the final citation network file 'auth_auth_citation_network.txt'. The final citation network contains the author-pair and their weight in each row. Each row of the final citation network looks like (a1 a2 w) means a1 cites a2, w number of times.
#sys.argv[1]=journal folder path
#sys.argv[2]=sorted_weighted_network
#sys.argv[3]=auth_auth_citation_network
#Input: sorted_weighted_network.txt(file that contains the sorted and weighted citation links with 'inside' or 'outside' labels)
#Output: auth_auth_citation_network.txt(file that contains the weighted author-author citation links or edges)

import sys


with open(sys.argv[1]+"/"+sys.argv[2]+".txt",mode='r') as f:
	for row in f:
		row=row.split()
		with open(sys.argv[1]+'/'+sys.argv[3]+'.txt',mode='a') as openfile:
			openfile.write(f'{row[1]} {row[2]} {row[0]}\n')
		
