import sys

print("Inderpreet Singh")
print("2104118")
print("\n")


def shortest_path_multistage(graph, N):
    n = len(graph)
    dp = [sys.maxsize] * n
    dp[n - 1] = 0 

    for i in range (N - 1, -1, -1):
        for j in range(n):
            if graph[j][0] == i:
                for neighbor, weight in graph[j][1]:
                    dp[j] = min(dp[j], weight + dp[neighbor])

    shortest_path_length = dp[0]

    return shortest_path_length

if __name__ == "__main__":
    
    graph = [
        (0, [(1, 2), (2, 7)]),
        (1, [(3, 1), (4, 4)]),
        (2, [(3, 3), (4, 1)]),
        (3, [(5, 2)]),
        (4, [(5, 3)]),
        (5, []),
    ]

    N = 6
    print("Shortest path length: ", shortest_path_multistage(graph, N))