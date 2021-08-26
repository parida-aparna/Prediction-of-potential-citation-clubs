#This program removes the redundant cliques from 'directed_cliques.txt' and outputs the maximal cliques.
#sys.argv[1]:specify folder path of journal
#sys.argv[2]:specify the input file i.e "directed_cliques.txt"
#Input: directed_cliques.txt (The file that contains the set of all directed cliques for the journal)
#Output: maximal_cliques.txt (The file that contains the set of all maximal cliques)

import sys

if __name__ == '__main__':
	
	f1 = open(sys.argv[1]+"/"+sys.argv[2],"r")#read the set of all directed cliques
	
	clique_list = []
	visited_cliques = []
	
	for clique in f1:
		clique=clique.split()
		clique_list.append(set(clique))#store all the cliques in a list
	
	c=0
	f2 = open(sys.argv[1]+"/maximal_cliques.txt","w")#output file to write the set of maximal cliques.
	
	
	for clique_set in clique_list:
		if len(visited_cliques)>0:
			#compare each clique with the cliques already visited
			if(all(not clique_set.issubset(cliques) for cliques in visited_cliques)): 					visited_cliques.append(clique_set)#append the maximal clique 
				
		else:
			visited_cliques.append(clique_set)#if the given clique is not visited add it
			
		c=c+1
		print(c)
	
	#Write all the maximal cliques which are in the visited_cliques list to the output file
	for clique in visited_cliques:
		for vertex in clique:
			f2.write(f'{vertex}\t')
		f2.write('\n')
		
	
