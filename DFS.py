
MAX_NODES = 10
adjacency_matrix = [[False] * MAX_NODES for _ in range(MAX_NODES)]
visited = [False] * MAX_NODES

def DFS(node, total_nodes):
    visited[node] = True
    print(node, end=" ")
    
    for i in range(total_nodes):
        if adjacency_matrix[node][i] and not visited[i]:
            DFS(i, total_nodes)

def main():
    total_nodes = int(input("Enter the number of nodes: "))
    edges = int(input("Enter the number of edges: "))
    
    # Initialize adjacency_matrix and visited
    for i in range(total_nodes):
        for j in range(total_nodes):
            adjacency_matrix[i][j] = False
        visited[i] = False
    
    print("Enter the edges (u, v):")
    for _ in range(edges):
        u, v = map(int, input().split())
        adjacency_matrix[u][v] = True
        adjacency_matrix[v][u] = True
    
    start_node = int(input("Enter the start node for DFS: "))
    print(f"DFS traversal starting from node {start_node}: ", end="")
    DFS(start_node, total_nodes)
    print()

if __name__ == "__main__":
    main()
