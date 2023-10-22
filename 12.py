import sys

print("Inderpreet Singh")
print("2104118")
print("\n")

cities = ["City A", "City B", "City C", "City D", "City E"]

distance_matrix = [
    [0, 10, 15, sys.maxsize, 20],
    [10, 0, sys.maxsize, 5, sys.maxsize],
    [15, sys.maxsize, 0, 9, 10],
    [sys.maxsize, 5, 9, 0, 12],
    [20, sys.maxsize, 10, 12, 0]
]

def floyd_warshall(cities, distance_matrix):
    n = len(cities)

    dist = [row[:] for row in distance_matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

min_distance_matrix = floyd_warshall(cities, distance_matrix)

print("Minimum distance between different cities: ")
for i in range (len(cities)):
    for j in range (len(cities)):
        if i != j:
            print(f"Distance from {cities[i]} to {cities[j]}: {min_distance_matrix[i][j]}")