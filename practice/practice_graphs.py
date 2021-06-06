def dfs(root, adj_matrix):
    path = []
    visited = [0 for _ in range(len(adj_matrix))]

    def rec(node, matrix):
        visited[node] = 1
        path.append(node)  # Pre order
        for adj_node in range(len(matrix)):
            if matrix[node][adj_node] == 1 and not visited[adj_node]:
                rec(adj_node, matrix)
        # path.append(node)  # Post order

    rec(root, adj_matrix)
    return path


def bfs(root, matrix):
    queue = [root]
    path = []

    while queue:
        node = queue.pop(0)
        path.append(node)
        for i, v in enumerate(matrix[node]):
            if v == 1:
                queue.append(i)
    return path


if __name__ == '__main__':
    """
              0
        1           2
    3       4   5       6
    
    """

    adj = [
        [0, 1, 1, 0, 0, 0, 0],  # 0

        [0, 0, 0, 1, 1, 0, 0],  # 1
        [0, 0, 0, 0, 0, 1, 1],  # 2

        [0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 0],  # 6
    ]
    print(dfs(0, adj))
    print(bfs(0, adj))
