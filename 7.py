print("Inderpreet Singh")
print("2104118")
print("\n")

import itertools

def calculate_distance(location1, location2):
    # Calculate the Euclidean distance between two locations
    x1, y1 = location1
    x2, y2 = location2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def find_minimum_route(locations):
    # Generate all possible permutations of the locations
    permutations = list(itertools.permutations(locations))

    # Initialize variables for the minimum distance and route
    min_distance = float('inf')
    min_route = None

    # Iterate through each permutation and calculate the total distance
    for perm in permutations:
        distance = 0
        for i in range(len(perm) - 1):
            distance += calculate_distance(perm[i], perm[i + 1])

        if distance < min_distance:
            min_distance = distance
            min_route = perm

    return min_route, min_distance

# Example usage
locations = [(0, 0), (1, 2), (2, 4), (3, 1)]
min_route, min_distance = find_minimum_route(locations)

print("Minimum Route:", min_route)
print("Minimum Distance:", min_distance)
