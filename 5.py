import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, cost):
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    def prim_mst(self):
        min_cost = 0
        visited = [False] * self.vertices
        heap = []

        heapq.heappush(heap, (0, 0))

        while heap:
            cost, current_vertex = heapq.heappop(heap)

            if visited[current_vertex]:
                continue

            visited[current_vertex] = True
            min_cost += cost

            for neighbor, edge_cost in self.graph[current_vertex]:
                if not visited[neighbor]:
                    heapq.heappush(heap, (edge_cost, neighbor))

        return min_cost


num_cities = int(input("Enter the number of cities: "))
num_connections = int(input("Enter the number of connections: "))

graph = Graph(num_cities)

print("Enter the connections in the format: 'city1 city2 cost'")
for _ in range (num_connections):
    city1, city2, cost = map(int, input().split())
    graph.add_edge(city1, city2, cost)
        
minimum_cost = graph.prim_mst()
print("The minimum cost to connect all cities: ", minimum_cost)

