def dfs(root, matrix):
    path = []
    visited = [0 for _ in range(len(matrix))]

    def rec(n, m):
        visited[n] = 1
        path.append(n)  # Pre order
        for j in range(len(m)):
            if m[n][j] == 1 and not visited[j]:
                rec(j, m)
        # path.append(n)  # Post order

    rec(root, matrix)
    return path


if __name__ == '__main__':

    """
        0
    1       2
    3
    
    """

    adj = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    print(dfs(0, adj))
