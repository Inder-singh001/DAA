print("Inderpreet Singh")
print("2104118")
print("\n")

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, start):
        distance = [float('inf')] * self.V
        distance[start] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        for u, v, w in self.graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print("Negative weight cycle detected.")
                return

        return distance

# Example usage
g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, -6)
g.add_edge(3, 4, 2)

start = 0
end = 4

shortest_distances = g.bellman_ford(start)
if shortest_distances[end] == float('inf'):
    print("No path found.")
else:
    print(f"The shortest distance from home to college is {shortest_distances[end]}.")
