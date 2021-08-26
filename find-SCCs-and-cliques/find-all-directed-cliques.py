#This program finds all the cliques within the largest scc of size>=3.
#cliques_python1 finds the directed cliques.
#sys.argv[1]-->journal folder path
#Input: largest_scc.txt (The file that contains the largest SCC of the given journal)
#Output: directed_cliques.txt (The file that contains the set of all directed cliques)

import networkx
import sys
import cliques_python as cp

def uniq(lst):
	last = object()
	for item in lst:
		if item == last:
			continue
		yield item
		last = item

def sort_and_deduplicate(l):
	return list(uniq(sorted(l)))

#This function returns the key of the dictionary when the value is given as input.
def get_key(val): 
	for key, value in nodes_dictionary.items(): 
		if val == value: 
			return key

graph = networkx.DiGraph()#Initialize a directed graph

f3=open(sys.argv[1]+"/directed_cliques.txt","w")#output file where the cliques are written.
graph = networkx.read_gpickle(sys.argv[1]+"/auth_auth_citation.gpickle")#read the directed citation network.

vertices = []#stores the set of vertices in the largest SCC.
nodes_dictionary={}#Every author-id is assigned a key value from 0 to N-1 where N is the number of authors.

f1 = open(sys.argv[1]+'/largest_scc.txt', mode = 'r')#read the largest SCC
	
for vertex_list in f1:
	vertex_list=vertex_list.split(',')
	no_of_vertices = len(vertex_list)
	print(no_of_vertices)
	for vertex in vertex_list:
		vertex1=int(vertex)
		vertices.append(str(vertex1))
		
subg = graph.subgraph(vertices)#find the induced subgraph of the citation network using the vertices of largest SCC.
edges = []#stores the edgelist of the induced subgraph

	
for e in subg.edges():
	edge = list(e)
	edges.append(edge)
edges=sort_and_deduplicate(edges)#sort the edges
	
cp.find_directed_cliques(f3, no_of_vertices, edges)#find directed cliques from the edges of the largest SCC
