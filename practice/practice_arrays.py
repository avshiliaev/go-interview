def reverse_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    left, right = 0, len(arr) - 1

    while True:
        if left >= right:
            return arr
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotate_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 2

    for i in range(k):
        for j in range(len(arr) - 1):
            ind = j
            arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]

    return arr


def rotate_matrix():
    # Reverse on Diagonal and then Reverse Left to Right
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    n = len(matrix)
    for row in range(n):
        for col in range(row, n):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    return [row[::-1] for row in matrix]


if __name__ == '__main__':
    print(rotate_array())
    print(reverse_array())

    for i in rotate_matrix():
        print(i)
