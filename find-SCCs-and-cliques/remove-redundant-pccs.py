#This program removes all the redundant PCCs
#sys.argv[1]:specify folder path of journal
#sys.argv[2]:specify threshold of intersection
#Input: redundant_pccs_t.txt (This file contains all the PCCs, where 't' is the threshold)
#Output: pccs_t.txt (This file contains all the non redundant PCCs, where 't' is the threshold)

import sys
import collections

if __name__ == '__main__':
	
	f1 = open(sys.argv[1]+"/redundant_pccs_"+sys.argv[2]+".txt","r")#sys.argv[1]:specify name of journal
	
	pcc_list = []
	visited_pccs = []
	
	for pcc in f1:
		pcc=pcc.split()
		pcc_list.append(set(pcc))#add each clique to the list
		
	c=0
	f2 = open(sys.argv[1]+"/pccs_"+sys.argv[2]+".txt","w")#sys.argv[1]:specify threshold
	
	
	for pcc_set in pcc_list:
		if len(visited_pccs)>0:
			if(all(not(pcc_set==pccs) for pccs in visited_pccs)): 					visited_pccs.append(pcc_set)#append only if the PCC is not redundant
			else:
				print(pcc_set)	
		else:
			visited_pccs.append(pcc_set)#append the unvisited pcc
			
		c=c+1
		print(c)
		
	#Write all the resultant PCCs 
	for pcc_set in visited_pccs:
		for vertex in pcc_set:
			f2.write(f'{vertex}\t')
		f2.write('\n')
		
	
