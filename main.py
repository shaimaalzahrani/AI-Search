from collections import deque
import heapq
import time

# ----------------------------
# Expanded Graph (more realistic)
# ----------------------------
graph = {
    "start": ["pcr", "blood", "xray"],
    "pcr": ["diagnosis"],
    "blood": ["xray", "urine"],
    "xray": ["ct_scan", "diagnosis"],
    "urine": ["diagnosis"],
    "ct_scan": ["diagnosis"],
    "diagnosis": []
}

goal = "diagnosis"

# ----------------------------
# Heuristic (for A*)
# lower = closer to diagnosis
# ----------------------------
heuristic = {
    "start": 3,
    "pcr": 1,
    "blood": 2,
    "xray": 1,
    "urine": 2,
    "ct_scan": 1,
    "diagnosis": 0
}

# ----------------------------
# BFS Algorithm (with metrics)
# ----------------------------
def bfs(start, goal):
    start_time = time.time()
    queue = deque([[start]])
    nodes_explored = 0
    explored_order = []

    while queue:
        path = queue.popleft()
        node = path[-1]
        nodes_explored += 1
        explored_order.append(node)

        if node == goal:
            end_time = time.time()
            return path, nodes_explored, explored_order, end_time - start_time

        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    return None, nodes_explored, explored_order, 0


# ----------------------------
# A* Algorithm (with metrics)
# ----------------------------
def astar(start, goal):
    start_time = time.time()
    queue = []
    heapq.heappush(queue, (0, [start]))
    nodes_explored = 0
    explored_order = []

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]
        nodes_explored += 1
        explored_order.append(node)

        if node == goal:
            end_time = time.time()
            return path, nodes_explored, explored_order, end_time - start_time

        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)

            g = len(new_path)
            h = heuristic[neighbor]
            f = g + h

            heapq.heappush(queue, (f, new_path))

    return None, nodes_explored, explored_order, 0


# ----------------------------
# Run and Compare
# ----------------------------
if __name__ == "__main__":
    print("=== Search Algorithms Comparison ===\n")

    bfs_path, bfs_nodes, bfs_explored, bfs_time = bfs("start", goal)
    print("BFS Result:")
    print("Result Path:", " → ".join(bfs_path))
    print("Explored order:", " → ".join(bfs_explored))
    print("Nodes explored:", bfs_nodes)
    print("Time:", round(bfs_time, 6), "seconds\n")

    astar_path, astar_nodes, astar_explored, astar_time = astar("start", goal)
    print("A* Result:")
    print("Result Path:", " → ".join(astar_path))
    print("Explored order:", " → ".join(astar_explored))
    print("Nodes explored:", astar_nodes)
    print("Time:", round(astar_time, 6), "seconds")