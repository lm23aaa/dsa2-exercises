import networkx as nx
import matplotlib.pyplot as mp

G = nx.Graph()

nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

# G.add_edge("A", "E", weight=8)
# G.add_edge("B", "B")
# G.add_edge("C", "D", weight=15)

G.add_weighted_edges_from([
    ("A", "E", 8),
    ("B", "B", 1),
    ("C", "D", 15)
])

# set layout to circular
pos = nx.circular_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_color='#ffffff', node_size=300, edgecolors='#000000', linewidths=1.5)

# edges
nx.draw_networkx_edges(G, pos, style='solid', width=2.0, edge_color='#ff0000')

# node labels
nx.draw_networkx_labels(G, pos, font_size=10)

# edge labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)

mp.show()
