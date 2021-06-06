def sliding_window(arr):
    # if the entire array meets the condition:
    if len(set(arr)) == 1:
        return len(arr)

    # Set the left to the beginning...
    left, result = 0, 0
    # ...and the right as running iterator over the entire collection:
    for right in range(len(arr)):

        # Calculate if the condition is met on a slice left to right
        n_uniques = len(set(arr[left:right]))

        # if we are right at the condition, we update the result:
        if n_uniques == 1:
            result = len(arr[left:right])
        # if we over the condition, we slide the window from the left:
        elif n_uniques > 1:
            left += 1
        # if we under the condition, we slide from the right
    return result


if __name__ == '__main__':
    # Find the longest subsequence:
    array = [0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9]  # 4 (3, 3, 3, 3,)
    print(sliding_window(array))
