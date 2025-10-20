import networkx as nx

def permutations(arr):
    # source: https://www.geeksforgeeks.org/python/generate-all-the-permutation-of-a-list-in-python
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    res = []
    for i in range(len(arr)):
        elem = arr[i]
        rem = arr[:i] + arr[i+1:]
        for p in permutations(rem):
            res.append([elem] + p)
    return res

def tsp(graph, start, undirected = True):
    # get nodes from the nx graph, turn it to a list
    nodes = list(graph.nodes())

    # set empty routes and costs
    routes = []
    costs = []

    # remove start element from nodes
    nodes.remove(start)

    # loop each permutation of the list of nodes
    for perm in permutations(nodes):
        # create new list with start being first and last elements
        route = [start] + perm + [start]
        
        # set initial cost to zero
        cost = 0

        # is route
        is_route = True

        # if the graph is undirected, then the check will
        # see if the route in reverse is not in the routes list
        # so as not to include duplicates
        # if the graph is directed, then it will simply
        # check if the route is already in routes
        if route[::-1 if undirected else 1] not in routes:
            # for each city in the route by index
            for i in range(0, len(route) - 1):
                # check the index plus 1 doesn't overflow
                # and the route exists
                if i + 1 != len(route) and graph.get_edge_data(route[i], route[i + 1]) != None:
                    # up the cost of the route
                    cost += int(graph.get_edge_data(route[i], route[i + 1])["weight"])
                else:
                    # set is_route to false to block the addition to lists
                    is_route = False

            if is_route:
                # apend this route
                routes.append(route)

                # append our cost to the costs list
                costs.append(cost)

    # prints routes and costs
    # print(routes, costs)
                
    # find the index of the minimum cost
    min_cost_index = costs.index(min(costs))

    # return the route and cost at the minimum cost index
    # as the indexes should match between the two lists
    return costs[min_cost_index], routes[min_cost_index]

# TESTING GRAPH 1
# undirected graph
# G = nx.Graph()

# add nodes
# G.add_nodes_from(["paris", "nantes", "marseille", "lyon"])

# # add edges
# G.add_weighted_edges_from([
#     ("paris", "nantes", 34),
#     ("paris", "marseille", 45),
#     ("paris", "lyon", 33),
#     ("nantes", "lyon", 29),
#     ("nantes", "marseille", 41),
#     ("marseille", "lyon", 15),
# ])
# TESTING GRAPH 1 END

# TESTING GRAPH 2
# undirected graph
G = nx.DiGraph()

# add nodes
G.add_nodes_from(["paris", "nantes", "marseille", "lyon"])

# # add edges
G.add_weighted_edges_from([
    ("paris", "nantes", 34),
    ("paris", "marseille", 33),
    ("marseille", "paris", 41),
    ("lyon", "marseille", 15),
    ("nantes", "lyon", 29),
    ("lyon", "nantes", 37),
    ("paris", "lyon", 33),
    ("nantes", "marseille", 41),
])
# TESTING GRAPH 2 END

# TESTING GRAPH 3
# undirected graph
# G = nx.Graph()

# add nodes
# G.add_nodes_from(["london", "edinburgh", "belfast", "cardiff"])

# # add edges
# G.add_weighted_edges_from([
#     ("london", "edinburgh", 634),
#     ("london", "belfast", 581),
#     ("london", "cardiff", 211),
#     ("edinburgh", "belfast", 231),
#     ("edinburgh", "cardiff", 497),
#     ("belfast", "cardiff", 391),
# ])
# TESTING GRAPH 3 END

print(tsp(G, "paris", True))