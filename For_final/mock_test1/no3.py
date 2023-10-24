'''
Define a recursive function find_route_distance to calculate a distance of a route 
when given its start node. That is given a start node and a dictionary as given in Questoin2,
the function find_route_distance traverses from the start node through each connected path along
the route recursively until it reaches the end of the route, while calculating the distance of
the route.
'''
routes = {
    "i": ("j", 4.0),
    "a": ("b", 3.4),
    "j": ("k", 6.0),
    "c": ("d", 5.6),
    "b": ("c", 4.0)
}

def find_route_distance(node, routes, sum=0):
    if node not in routes:
        return sum
    else:
        sum += routes[node][1]
        return find_route_distance(routes[node][0], routes, sum)
        
    
print(find_route_distance("a", routes))
print(find_route_distance("b", routes))