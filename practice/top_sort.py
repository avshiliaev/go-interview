def top_sort(graph_):
    # https://stackoverflow.com/a/62758232/10202443
    # https://sharmaeklavya2.github.io/theoremdep/nodes/graph-theory/dfs/toposort.html
    visited = {}
    result = []

    # 1. Transpose
    transposed_graph_ = {k: [] for k, v in graph_.items()}
    for k, v in graph_.items():
        for val in v:
            transposed_graph_[val].append(k)

    # 2. Define dfs
    def dfs(node):
        if visited.get(node, False):
            return
        visited[node] = True
        for adj in transposed_graph_[node]:
            dfs(adj)
        result.append(node)

    # 3. Dfs through each node
    for i in transposed_graph_.keys():
        dfs(i)

    return result


if __name__ == '__main__':
    """
    a -->-- b -->-- d -->-- e
     \             /
      -->-- c -->--
    """
    # why the graph has to be transposed: https://stackoverflow.com/a/67291884/10202443
    graph_one = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e'],
        'e': [],
    }
    # [a, b, c, d, e]

    # https://www.geeksforgeeks.org/python-program-for-topological-sorting/#:~:text=Topological%20sorting%20for%20Directed%20Acyclic,4%202%203%201%200%E2%80%9D.
    graph_two = {
        5: [0, 2],
        4: [0, 1],
        3: [1],
        2: [3],
        1: [],
        0: []
    }
    # 5 4 2 3 1 0

    print(top_sort(graph_one))
    print(top_sort(graph_two))
