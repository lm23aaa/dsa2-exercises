# G = (V, E), V = {a,b,c,d,e}, E = {(a,b), (b,c), (c,d), (d,a)}
import networkx as nx
import matplotlib.pyplot as mp

# Directed Graph
G = nx.DiGraph()

# Nodes
nodes = ['a','b','c','d']
G.add_nodes_from(nodes)

# Edges
edges = [
    ('a','b'), 
    ('b','c'), 
    ('c','d'), 
    ('d','a')
]
G.add_edges_from(edges)

# set layout to circular
pos = nx.circular_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_color='#ffffff', node_size=300, edgecolors='#000000', linewidths=1.5)

# edges
nx.draw_networkx_edges(G, pos, style='solid', width=2.0, edge_color='#010101', arrowsize=17)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10)

mp.show()

