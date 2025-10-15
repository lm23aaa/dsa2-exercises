import networkx as nx
import matplotlib.pyplot as mp

# directed graph
G = nx.DiGraph()

nodes = ["A","B"]

G.add_nodes_from(nodes)

G.add_edge("A","B",weight=3)

# set layout to circular
pos = nx.circular_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_color='#ffffff', node_size=300, edgecolors='#000000', linewidths=1.5)

# edges
nx.draw_networkx_edges(G, pos, style='dashed', width=2.0, edge_color='#ff0000', arrowsize=17)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10)

# edge labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)

mp.show()