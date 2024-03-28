import itertools

# Function to calculate the distance between two cities
def distance(city1, city2):
    return distance_matrix[city1][city2]

# Function to calculate the total distance of a route
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    total += distance(route[-1], route[0])  # Return to the starting city
    return total

# Function to find the shortest route
def tsp(cities):
    shortest_route = None
    min_distance = float('inf')
    permutations = itertools.permutations(cities)
    for route in permutations:
        route_distance = total_distance(route)
        if route_distance < min_distance:
            min_distance = route_distance
            shortest_route = route
    return shortest_route, min_distance

# Example usage:
# Sample input: Cities and their distances
distance_matrix = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
cities = ['A', 'B', 'C', 'D']
shortest_route, min_distance = tsp(cities)
print("Shortest route:", shortest_route)
print("Minimum distance:", min_distance)


#output
Shortest route: ('A', 'B', 'D', 'C')
Minimum distance: 80
