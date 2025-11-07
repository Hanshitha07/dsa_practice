def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Same graph
graph = {
    'A': ['B', 'C', 'G'],
    'B': ['A', 'D', 'C'],
    'C': ['A', 'B', 'G', 'F'],
    'D': ['B', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['C', 'D', 'E'],
    'G': ['A', 'C','F']
}

print("DFS Traversal:", end=" ")
dfs(graph, 'A')
