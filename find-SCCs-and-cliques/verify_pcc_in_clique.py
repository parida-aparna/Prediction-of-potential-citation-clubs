#This program verifies if a PCC is a clique, not necessarily maximal clique 
#sys.argv[1]-->specify folder path of journal
#sys.argv[2]-->specify threshold
#Input: maximal_cliques.txt(file that contains the set of maximal cliques) and pccs_t.txt(file that contains the set of pccs with threshold 't')
#Output: predicted_citation_clubs_t.txt(file that contains the set of PCCs that were correctly predicted)

import sys

f1 = open(sys.argv[1]+"/maximal_cliques.txt", "r")
f2 = open(sys.argv[1]+"/pccs_"+sys.argv[2]+".txt", "r")
f3 = open(sys.argv[1]+"/predicted_citation_clubs_"+sys.argv[2]+".txt", "w")

clique_list = []

for clique in f1:
	clique = clique.split()
	clique = set(clique)
	clique_list.append(clique)

for pcc in f2:
	pcc = pcc.split()
	pcc = set(pcc)
	for clique in clique_list:
		if pcc.issubset(clique):#if PCC is a subset of a clique
			f3.write(f'{clique}\n')
	

