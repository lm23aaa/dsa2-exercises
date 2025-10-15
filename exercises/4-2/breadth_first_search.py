import networkx as nx
import matplotlib.pyplot as mp

def breadth_first_search(graph, target_node, starting_node, verbose = False):

    # Dictionary that contains node > which node we visited it from
    # Used during result construction to save time
    reverse_children = {}

    # Queue. Using a list, but only operations used are those of a FIFO queue
    # - Pop first element
    # - Append to the end
    nodes_to_process = []

    # Keep track of which nodes we have visited to avoid going back
    visited_nodes = []
        
    nodes_to_process.append(starting_node)

    while len(nodes_to_process) > 0:

        next_node = nodes_to_process.pop(0)
        if verbose:
            print("Next node to process is " + str(next_node))

        if next_node == target_node:
            if verbose:
                print("Found node")
            return get_return_path(reverse_children, next_node)

        # Get the children as: Any nodes connected to starting_node that are not already visited, as we don't want to go back
        children = [neighbour for neighbour in graph.neighbors(next_node) if neighbour not in visited_nodes]

        # Once we have the children, do 2 things
        # 1 Queue them to be processed
        for child in children:
            nodes_to_process.append(child)

        # 2 Add them to our reverse_children store, to keep track of from what node we visited them
        for child in children:
            reverse_children[child] = next_node

        # Mark next_node as visited
        visited_nodes.append(next_node)
        
    # If we run out of nodes, it's not in the graph
    return


def get_return_path(reverse_children, from_node):
    # reverse_hildren has information about which node we used to reach each node
    result = [from_node]
    next_node = from_node
    while next_node in reverse_children:
        result.append(reverse_children[next_node])
        next_node = reverse_children[next_node]

    result.reverse()
    return result


# RANDOM
# G = nx.random_labeled_tree(10, seed=42)
# RANDOM END

# BINARY
# G = nx.Graph()
# edges = [
#     (1, 2),
#     (1, 3),
#     (2, 4),
#     (2, 5),
#     (3, 6),
#     (3, 7)
# ]
# G.add_edges_from(edges)
# BINARY END

# STAR
# G = nx.Graph()
# edges = [
#     (1, 2),
#     (1, 3),
#     (1, 4),
#     (1, 5),
#     (1, 6),
#     (1, 7)
# ]
# G.add_edges_from(edges)
# STAR END

# CHAIN
G = nx.Graph()
edges = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8)
]
G.add_edges_from(edges)
# CHAIN END

if nx.is_tree(G):
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
    print(breadth_first_search(G, 7, 1, True))
    mp.show()