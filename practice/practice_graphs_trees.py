if __name__ == '__main__':

    """
          A
    B     C     D
    E   F   G   H
    I   J
    """
    graph = {
        "A": ["B", "C", "D"],
        "B": ["E"],
        "C": ["F", "G"],
        "D": ["H"],
        "E": ["I"],
        "F": ["J"]
    }
    binary_tree_one = {
        11: [6, 15],
        6: [3, 8],
        15: [13, 17],
        3: [1, 5],
        13: [12, 14],
        17: [19]
    }
    binary_tree_two = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "F": ["J", "K"],
        "G": ["L"]
    }


    def bfs_iterative(graph_, source):
        result = []
        path = [source]
        while path:
            # use as queue: add and take from different sides
            node = path.pop(0)
            result.append(node)
            path = path + graph_.get(node, [])
        return result


    def dfs_iterative(graph_, source):
        """
        PreOrder
        :param graph_:
        :param source:
        :return:
        """
        result = []
        path = [source]
        while path:
            # use as stack: add and take from the same side
            node = path.pop(0)
            result.append(node)
            path = graph_.get(node, []) + path
        return result


    def rec_dfs(graph_, node, stack):
        """
        PreOrder only cause not binary.
        :param graph_:
        :param node:
        :param stack:
        :return:
        """
        if node not in stack:
            stack.append(node)
            if node not in graph_:
                # leaf node, backtrack
                return stack
            for neighbour in graph_[node]:
                stack = rec_dfs(graph_, neighbour, stack)
        return stack


    order_result = []


    def rec_dfs_binary_only(graph_, node, stack):
        """
        Can control order because recursive and binary.
        :param graph_:
        :param node:
        :param stack:
        :return:
        """
        if node not in stack:
            stack.append(node)
            # Three cases possible.
            # We control if it is printed before, in-between of after:

            children = graph_.get(node, [])
            if not children:
                # leaf node, backtrack
                order_result.append(node)
                return stack
            elif len(children) == 1:
                stack = rec_dfs_binary_only(graph_, children[0], stack)
                order_result.append(node)
            else:
                stack = rec_dfs_binary_only(graph_, children[0], stack)
                order_result.append(node)
                stack = rec_dfs_binary_only(graph_, children[1], stack)
        return stack


    # preorder: [11, 6, 3, 1, 5, 8, 15, 13, 12, 14, 17, 19]
    print("DFS", dfs_iterative(binary_tree_two, "A"))

    rec_dfs_binary_only(binary_tree_one, 11, [])
    print("DFS", order_result)

    # print("BFS", bfs_iterative(binary_tree_one, 11))
