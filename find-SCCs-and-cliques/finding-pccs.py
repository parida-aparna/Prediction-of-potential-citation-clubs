#This program finds the PCCs by the pairwise union of maximal cliques with pairwise intersection greater than a given threshold.
#sys.argv[1]:specify folder path of journal
#sys.argv[2]-->threshold of intersection
#Input: maximal_cliques.txt (The file that contains the list of maximal cliques for the journal)
#Output: redundant_pccs_t.txt (The file that contains all the PCCs formed where 't' is the given threshold.)

import sys
from igraph import Graph


if __name__ == '__main__':
	
	f1 = open(sys.argv[1]+"/maximal_cliques.txt","r")#sys.argv[1]:specify name of journal
	
	clique_list = []
	visited_cliques = []
	
	for clique in f1: 
		clique=clique.split()
		clique_list.append(set(clique))#append each clique to a single list
	
	c=0
	
	f2 = open(sys.argv[1]+"/redundant_pccs_"+sys.argv[2]+".txt","w")#output file
	
	threshold = float(sys.argv[2])#sys.argv[2]-->threshold
	
	
	for clique_set in clique_list:
		maximum=0
		if len(visited_cliques)>0:
			for cliques in visited_cliques:
				weight=cliques.intersection(clique_set)
				if len(weight)>=(threshold*len(clique_set)): #threshold in terms of %
					for node in cliques.union(clique_set):
						f2.write(f'{node}\t')
					f2.write('\n')		
			visited_cliques.append(clique_set)
				
		else:
			visited_cliques.append(clique_set)
			
		c=c+1
		print(c)
		
	
	
	
	
