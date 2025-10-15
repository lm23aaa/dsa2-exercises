# G = (V, E), V = {1, 2}, E = {{1, 2}}
import networkx as nx
import matplotlib.pyplot as mp

# undirected graph
G = nx.Graph()

# add nodes (1.0)
G.add_node(1)
G.add_node(2)

# add edge (1.0)
G.add_edge(1,2)

# build & show graph
nx.draw(
    G, 
    with_labels=True,
    node_color='#ffffff',
    node_size=1000,
    edgecolors='#000000',
    linewidths=2.0,
    width=2.0,
    font_size=15
)
mp.show()