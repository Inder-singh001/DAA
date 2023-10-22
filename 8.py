import heapq

def dijkstra(graph, start, end):
    # Initialize distance dictionary with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a priority queue (min-heap) for nodes to explore
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Ignore nodes that have already been processed
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance and add to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]

# Example road network represented as a graph (adjacency list)
road_network = {
    "Home": {"A": 5, "B": 2},
    "A": {"College": 7},
    "B": {"A": 8, "College": 3},
    "College": {}
}

start_location = "Home"
end_location = "College"

shortest_distance = dijkstra(road_network, start_location, end_location)

if shortest_distance == float('inf'):
    print("No path found.")
else:
    print(f"The shortest distance from {start_location} to {end_location} is {shortest_distance} units.")
