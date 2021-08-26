#This program builds a directed graph from the edges and its corresponding weights in 'auth_auth_citation_network.txt'. The graph is pickled to avoid repeated building of the directed graph each time the citation network needs to be accessed.
#sys.argv[1]-->specify journal folder path
#Input: auth_auth_citation_network.txt(file contains the edges and weights of the author citation network)
#Output: auth_auth_citation.gpickle(the author citation graph is pickled and stored)

import sys
import networkx as nx
import pickle


f1 = open(sys.argv[1]+'/auth_auth_citation.txt', mode='r')

#Initialize a directed graph
g = nx.DiGraph()
	
row_list=[]
for row in f1:
	row=row.split()
	#Each row contains a citation link and its corresponding weight
	#row[0]-->citer author, row[1]-->citee author, row[2]-->weight(no. of times citer has cited citee)
	g.add_edge(row[0],row[1],weight=int(row[2]))#Add the edges to the directed citation network.
	print(int(row[0]))
	print(int(row[1]))
	print(int(row[2]))

#pickle the citation network	
nx.write_gpickle(g, sys.argv[1]+"/auth_auth_citation.gpickle")	

