# Experiment D1: Graph Traversal (BFS and DFS)
# Problem: Visit city locations starting from 'A' using BFS (Adjacency List) and DFS (Adjacency Matrix).

nodes = ['A', 'B', 'C', 'D']

# Adjacency List for BFS
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Adjacency Matrix for DFS
adj_matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

def bfs(start):
    visited, queue = [], [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(adj_list[node])
    return visited

def dfs(idx, visited):
    visited.append(nodes[idx])
    for i in range(len(nodes)):
        if adj_matrix[idx][i] == 1 and nodes[i] not in visited:
            dfs(i, visited)
    return visited

if __name__ == "__main__":
    print("BFS (Adjacency List):", bfs('A'))
    print("DFS (Adjacency Matrix):", dfs(0, []))
