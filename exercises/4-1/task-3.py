# G = (V, E), V = {A,B,C}, E = {(A,C), (A,B), (C,B), (B,A), (B,C)}
import networkx as nx
import matplotlib.pyplot as mp

# Directed Graph
G = nx.DiGraph()

# Nodes
nodes = ['A','B','C']
G.add_nodes_from(nodes)

# Edges
edges = [
    ('A','C'), 
    ('A','B'), 
    ('C','B'), 
    ('B','A'), 
    ('B','C')
]
G.add_edges_from(edges)

# set layout to circular
pos = nx.circular_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_color='#ffffff', node_size=300, edgecolors='#000000', linewidths=1.5)

# edges
nx.draw_networkx_edges(G, pos, style=['dashed', 'dashed', 'solid', 'solid', 'dotted'], width=2.0, edge_color='#010101', arrowsize=17, connectionstyle='arc3,rad=0.1')

# node labels
nx.draw_networkx_labels(G, pos, font_size=10)

mp.show()

