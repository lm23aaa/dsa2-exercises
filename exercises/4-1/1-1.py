import networkx as nx
import matplotlib.pyplot as mp

# undirected graph
G = nx.Graph()

# add nodes (1.1)
nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

# add edges (1.1)
edges = [("A", "E")]
G.add_edges_from(edges)

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