print("Inderpreet Singh")
print("2104118")
print("\n")

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, cost):
        self.graph.append((u, v, cost))

    def find_parent(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find_parent(parent, parent[vertex])
    
    def union(self, parent, rank, vertex1, vertex2):
        root1 = self.find_parent(parent, vertex1)
        root2 = self.find_parent(parent, vertex2)

        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal_mst(self):
        self.graph.sort(key=lambda x : x[2])
        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices
        min_cost = 0

        for u, v, cost in self.graph:
            if self.find_parent(parent, u) != self.find_parent(parent, v):
                self.union(parent, rank, u, v)
                min_cost += cost

            return min_cost
        
def main():
    num_colleges = int(input("Enter the number of engineering Colleges: "))
    num_connections = int(input("Enter the number of connections: "))

    graph = Graph(num_colleges)

    print("Enter connection in the format: 'college1 college2 cost'")
    for _ in range(num_connections):
        college1, college2, cost = map(int, input().split())
        graph.add_edge(college1, college2, cost)

    minimum_cost = graph.kruskal_mst()
    print("Minimum cost to connect all engineering colleges: ", minimum_cost)

if __name__ == "__main__":
    main()