#This program generates the unweighted co-authorship links of the journal 
#sys.argv[1]-->journal folder path
#Input: journal_papers.txt(file that contains the paper-ids, author-ids and reference-ids of the journal 'j')
#Output: unweighted_co_auth.txt(file that contains the co-authorship links or edges)

import csv
import sys
import itertools 


with open(sys.argv[1]+"/unweighted_co_auth.txt",'w') as openfile:
	openfile.write('')


#This function finds all possible subsets of set 's'. The size of the subsets found is 'n'.
def findsubsets(s, n): 
	return list(itertools.combinations(s, n)) 


with open(sys.argv[1]+"/journal_papers.txt","r") as f:		
	csv_reader = csv.reader(f,delimiter=',')		
	for row in csv_reader:
		authors=row[1].split()#get the author ids of the row
		author_pairs=findsubsets(authors,2)#generate co-author pairs
		
		with open(sys.argv[1]+"/unweighted_co_auth.txt",mode='a') as openfile:
			for pair in author_pairs:#write the co-author pairs to a file
				openfile.write(f'{pair}\n')
				

		
		
					
		
			
		
		
		
		
		
		
		
		

