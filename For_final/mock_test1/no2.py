'''
Define a Python function find_route to find a route formed by connecting some directed
paths, each of which connects from one node to another. Given a start node of a route and
a dictionary, whose rows store directed path with their lengths (measured in centimeters),
the function traverses from the start node through each connected path and forms the route
until it reaches the end of the route, the function then returns the route (represented by a list of nodes
connected by the paths) and its distance.
'''
routes = {
    "i": ("j", 4.0),
    "a": ("b", 3.4),
    "j": ("k", 6.0),
    "c": ("d", 5.6),
    "b": ("c", 4.0)
}

def find_routes(node, routes):
    node_ls = [node]
    total_distance = 0
    while True:
        if node in routes:
            total_distance += routes[node][1]
            node = routes[node][0]
            node_ls.append(node)
            if node not in routes:
                break
    return (node_ls, total_distance)

print(find_routes("a", routes))
print(find_routes("b", routes))