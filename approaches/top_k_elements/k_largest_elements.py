from heapq import *


def find_k_largest(arr_, k_):
    min_heap = []

    # initialize a heap of length k_
    for i in range(k_):
        heappush(min_heap, arr_[i])

    # push on to he heap and re-balancing
    for i in range(k_, len(arr_)):
        if arr_[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, arr_[i])

    # We can sort it for simplicity because in a min_heap:
    # 1. The root will be at arr[0].
    # 2. For any i element:
    #   - arr_[(i -1) / 2] returns its parent node.
    #   - arr_[(2 * i) + 1] returns its left child node.
    #   - arr_[(2 * i) + 2] returns its right child node.
    # But we can keep it though ¯\_(ツ)_/¯
    result = sorted(min_heap)
    return result


if __name__ == '__main__':
    print(find_k_largest([0, 1, 100, 100, 100], 4))
    print(find_k_largest([1, 3, 4, 2, 6, 1, 8, 5, 9, 7, 3, 1, 2, 7, 8], 3))
    print(find_k_largest([i for i in range(1000)], 10))  # All different
    print(find_k_largest([9 for i in range(1000)], 10))  # All same

    # [1, 100, 100, 100]
    # [7, 8, 9]
    # [990, 991, 992, 993, 994, 995, 996, 997, 998, 999]
    # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
