#This program finds the collaboration density of the maximal cliques
#sys.argv[1]-->specify folder path of the journal
#Input: co_auth.txt(The file that contains the set of co-authorsip edges) and maximal_cliques.txt(file that contains the set of all maximal cliques)
#Output: collaboration_density_in_cliques.txt(file that contains the collaboration density of each maximal clique) and co_authors_in_cliques.txt(file that contains the set of co_authors for each clique)

import itertools
import sys

#This function finds subsets of items in 's'. The size of each subset is 'n'.
def findsubsets(s, n): 
	return list(itertools.combinations(s, n)) 

f1=open(sys.argv[1]+"/co_auth.txt",mode='r')
f3=open(sys.argv[1]+"/co_authors_in_cliques.txt",mode='w')
f4=open(sys.argv[1]+"/collaboration_density_in_cliques.txt",mode='w')

auth_list=[]

for row in f1:
	row=row.split()
	co_auth_set=set()
	co_auth_set.add(row[0])#append the first author of the co-author pair 
	co_auth_set.add(row[1])#append the second author of the co-author pair
	auth_list.append(co_auth_set)#append all co-author pairs to a list

with open(sys.argv[1]+"/maximal_cliques",mode='r') as f2:
	for row in f2:
		collaborations=0
		row=row.split()#each row is a clique
		subset=findsubsets(row,2)#generate author pairs from the author nodes in the clique
		subset_size=len(subset)
		
		for s in subset:	
			co_auth_pair=set()
			co_auth_pair.add(s[0])
			co_auth_pair.add(s[1])
			
			for auth_pair in auth_list:
				#check how many co_auth_pairs are in auth_list(which is the set of all author pairs of co_auth.txt)
				if co_auth_pair.issubset(auth_pair):
					f3.write(f'{co_auth_pair} ')
					collaborations=collaborations+1
					break
					
		f3.write('\n')
		collaboration_density=collaborations/subset_size
		f4.write(f'{collaboration_density}\n')
			
