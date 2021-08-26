#Python implementation to finding SCCs using networkx library functions
#sys.argv[1]-->specify journal folder path
#Input:auth_auth_citation.gpickle(file contains the pickled version of the citation network)
#Output:SCCs.txt(file contains all the SCCs obtained for the author citation network) and SCCs_lengths.txt(file that contains the length of each SCC)

import sys
import networkx

if __name__ == '__main__':
	
	f1 = open(sys.argv[1]+'/SCCs.txt', mode='w')#stores the SCCs
	f2 = open(sys.argv[1]+'/SCCs_lengths.txt', mode='w')#stores the length of each SCC
	graph = networkx.read_gpickle(sys.argv[1]+"/auth_auth_citation.gpickle")#read the graph
	scc = networkx.strongly_connected_components(graph)#find SCCs from the citation network.
	
	for i in scc:
		f1.write(f'{i}\n')
		f2.write(f'{len(i)}\n')
	

