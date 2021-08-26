# Prediction-of-potential-citation-clubs

Detection of citation clubs is a first step toward understanding the 
dynamics of citations and the relationships between authors that
cite each other. There is increased interest in detecting citation clubs in
the recent times as the citation index of authors and impact factors of 
journals are being considered as performance indicators in academics.
A citation network, G is a directed and weighted network where each node
represents an author a_i and there exists an edge (a_i,a_j), if a_i 
cites a paper written by a_j. The weight w on the edge represents the 
number of citations. A citation club, C
A citation club, C is a group of authors that are 
tightly bonded and cite each others' work. In other words, a citation club 
is defined as a directed maximal clique of size>=3 within a strongly 
connected component of the citation network, G. A potential 
citation club (PCC) is a group of authors that are likely to form cliques in 
future.

In this work an algorithm is proposed that finds citation clubs within the 
largest SCC of the citation network. The data is the set of papers published in an open access journal OJ and a closed access journal CJ from DBLP between years 2000-2020. It was observed that 5389 citation clubs
ranging from sizes 3 to 12 were formed for OJ and 1348 citation clubs 
ranging from sizes 3 to 11 were formed in CJ. 
In this paper, an algorithm was proposed to detect PCCs from the existing 
citation clubs in two journals -- one open access (OJ) and another a closed
access one (CJ). An ML based approach to link prediction was used to
generate the features of the train and 
test sets. A random forest classifier was used for training. The model was 
tested with the test set and it was observed that all the test links were 
correctly predicted. The predicted test links were added to the train graph 
links and citation clubs determined. It was observed that the citation clubs 
in OJ and CJ were predicted with 98% precision and a recall of 95% for OJ 
and 78% for CJ.
