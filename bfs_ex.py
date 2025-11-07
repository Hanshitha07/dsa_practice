from collections import deque

def bfs(graph, start):
    visited = set()              # To keep track of visited nodes
    queue = deque([start])       # Use queue for BFS
    result = []                  # To store traversal order

    while queue:
        node = queue.popleft()   # Remove from front of queue
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add all unvisited neighbors to queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

# Example graph represented as adjacency list
graph = {
    'A': ['B', 'C', 'G'],
    'B': ['A', 'D', 'C'],
    'C': ['A', 'B', 'G', 'F'],
    'D': ['B', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['C', 'D', 'E'],
    'G': ['A', 'C','F']
}

print("BFS Traversal:", bfs(graph, 'A'))
