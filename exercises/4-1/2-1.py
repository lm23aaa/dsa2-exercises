import networkx as nx
import matplotlib.pyplot as mp
 
# directed graph 
G = nx.DiGraph()
 
nodes=["A","B"]
 
G.add_nodes_from(nodes)
 
G.add_edge("A","B")
G.add_edge("B","A")
 
# Layout set to circular 
pos= nx.circular_layout(G)
 
# Nodes
nx.draw_networkx_nodes(G,pos)
 
# Edges
nx.draw_networkx_edges(G, pos, style=['solid','dotted'], connectionstyle='arc3,rad=0.5')

# Node labels
nx.draw_networkx_labels(G, pos)

mp.show()