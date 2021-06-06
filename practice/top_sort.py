def iterative_topological_sort(graph_, root):
    """
    Two stacks because we have two DFSs:
        see why here https://www.geeksforgeeks.org/topological-sorting/
        and here https://stackoverflow.com/a/47234034/10202443

        in fact this is correct: https://stackoverflow.com/a/67291884/10202443
        instead of choosing the root arbitrary, we want to transpose the graph first and then get a node which has
        NO incoming edges.

    :param graph_:
    :param root:
    :return:
    """
    seen = set()
    order = []
    stack_one = [root]
    stack_two = []
    while stack_one:
        node = stack_one.pop(-1)
        if node not in seen:
            seen.add(node)
            stack_one += graph_[node]
            while stack_two and node not in graph_[stack_two[-1]]:
                order.insert(0, stack_two.pop(-1))
            stack_two.append(node)

    return stack_two + order


if __name__ == '__main__':
    """
    a -->-- b -->-- d -->-- e
     \             /
      -->-- c -->--
    """
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e'],
        'e': []
    }
    # [a, b, c, d, e]

    print(iterative_topological_sort(graph, 'a'))
