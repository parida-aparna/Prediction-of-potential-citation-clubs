#This program finds the directed cliques within the citation network.

MAX = 10000; 

# Stores the vertices 
store = [-1] * MAX; 

# Graph 
graph = [[0 for i in range(MAX)] for j in range(MAX)]; 

# Degree of the vertices 
d = [0] * MAX; 

#Returns the key for a given value of the dictionary
def get_key(val): 
	for key, value in Nodes_Dictionary.items(): 
		if val == value: 
			return key


Nodes_Dictionary={}
edgeset=set()

#Build a dictionary that assigns a key to each author-id. Key ranges from 0 to |author_ids|-1
def make_key_value_pairs(edges):
	key=0
	for edge in edges:
		edgeset.add(edge[0])
		edgeset.add(edge[1])
	while len(edgeset)!=0:
		Nodes_Dictionary[key]=edgeset.pop()
		key=key+1
	
	
def is_clique(b): 

	# Run a loop for all set of edges 
	for i in range(1, b): 
		for j in range(i + 1, b): 

			# If any edge is missing or if same nodes are considered return False
			if (graph[store[i]][store[j]] == 0 or graph[store[j]][store[i]] == 0 or store[i]==store[j]): 
				return False; 
	
	return True; 

# Function to find all the sizes of maximal cliques 

def maxCliques(i, l,n): 
	print(i,l,n)
	# Maximal clique size 
	max_ = 0; 

	# Check if any vertices from i+1 
	# can be inserted 
	for j in range(i, n): 

		# Add the vertex to store 
		if store[l-1]!=j:
			store[l] = j; 

			# If the graph is not a clique of size k then 
			# it cannot be a clique by adding another edge 
			
			if (is_clique(l+1)): 

				# Update max 
				max_ = max(max_, l); 

				# Check if another edge can be added 
				max_ = max(max_, maxCliques(j, l + 1,n)); 
				
	return max_; 
	

#Writes a clique to the output file	
def print_cli(f1,n) :  
	f1.write('{');
	for i in range(1, n) : 
		f1.write(f'{Nodes_Dictionary[store[i]]}\t') 
	f1.write("},\n")
  
# Function to find all the cliques of size s  
def findCliques(f1,i, l, s,n) : 
  
    # Check if any vertices from i+1 can be inserted  
	for j in range( i , n -(s - l)) :  
  
        # If the degree of the graph is sufficient  
		if (d[j] >= s - 1) : 
  
            # Add the vertex to store  
			if store[l-1]!=j:
				store[l] = j;  
	  
				    # If the graph is not a clique of size k  
				    # then it cannot be a clique  
				    # by adding another edge  
				if (is_clique(l + 1)) : 
	  
				# If the length of the clique is  
				# still less than the desired size  
					if (l < s) : 
	  
		            # Recursion to add vertices  
						findCliques(f1,j, l + 1, s,n);  
	  
		        # Size is met  
					else : 
						print_cli(f1,l + 1);  


# Driver code 
def find_directed_cliques(f1:str, n, edgelist): 
   
	make_key_value_pairs(edgelist)
	edges=[]
	for edge in edgelist:
		edge1=[]
		edge1.append(get_key(edge[0]))
		edge1.append(get_key(edge[1]))
		edges.append(edge1)
	size = len(edges); 
	print(f'Size:{size}')
	
	#Build the adjacency matrix for the edges in the citation network
	for i in range(size): 
		graph[edges[i][0]][edges[i][1]] = 1;
		d[edges[i][0]] += 1; 
	
	#k returns the size of the maximum clique in the largest SCC.	
	k=maxCliques(0, 1,n); 
	
	#find all cliques of size>=3 till the maximum clique.
	while k>=3:
		findCliques(f1,0, 1, k,n);
		k=k-1
		f1.write('\n')
	
