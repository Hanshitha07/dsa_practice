# Directed Weighted Graph using Adjacency Matrix (Simple Input Format)

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Take vertex names
vertices = []
for i in range(n):
    v = input(f"Enter name of vertex {i+1}: ").strip()
    vertices.append(v)

# Initialize adjacency matrix with 0 (no edge)
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

# Input number of edges
edges = int(input("Enter number of edges: "))

print("\nEnter each edge in the format: source destination weight")
print("Example: A B 3 (means A → B with weight 3)\n")

# Take each edge in a single line
for _ in range(edges):
    u, v, w = input("Enter edge: ").split()
    w = int(w)
    i = vertices.index(u)
    j = vertices.index(v)
    adj_matrix[i][j] = w

# Display adjacency matrix
print("\nDirected Weighted Graph (Adjacency Matrix):")
print("   ", "  ".join(vertices))
for i in range(n):
    print(vertices[i], adj_matrix[i])
