# G = (V, E), V = {A,B,C,Z}, E = {{A,C}, {C,Z}, {B,Z}}
import networkx as nx
import matplotlib.pyplot as mp

# Undirected Graph
G = nx.Graph()

# Nodes
nodes = ['A','B','C','Z']
G.add_nodes_from(nodes)

# Edges
edges = [
    ('A','C'), 
    ('C','Z'), 
    ('B','Z')
]
G.add_edges_from(edges)

# set layout to circular
pos = nx.circular_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_color='green', node_size=300, edgecolors='green', linewidths=1.5)

# edges
nx.draw_networkx_edges(G, pos, style='solid', width=2.0, edge_color='black', arrowsize=17)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

mp.show()

