def longest_subsequence(arr):
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
        else:
            # if we under the condition, we let the window slide from the right (we need more):
            continue
    return result


def max_sum(arr, k):
    if len(arr) <= 3:
        return sum(arr)

    left, result = 0, 0
    for right in range(len(arr)):
        sum_ = sum(arr[left:right])

        # 'right at the condition' is optional (not applicable here):

        # if we over the condition, we slide the window from the left:
        if sum_ > result:
            result = sum_
            left += 1
        else:
            # if we under the condition, we let the window slide from the right (we need more):
            continue

    return result


def max_average(arr, k):
    left, result = 0, (0, [])
    for right in range(1, len(arr)):

        # if we over the condition, we slide the window from the left:
        # The key is to find the right condition!
        if right - left >= k:
            average = sum(arr[left:right]) / len(arr[left:right])
            if average > result[0]:
                result = (average, arr[left:right])
            left += 1
        else:
            # if we under the condition, we let the window slide from the right (we need more):
            continue
    return result


if __name__ == '__main__':
    # Find the longest subsequence:
    array = [0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9]  # 4 (3, 3, 3, 3,)
    print(longest_subsequence(array))

    # Find the max sum of length 3:
    array = [1, 0, 3, 5, 1, 3, 9, 8, 1, 2]  # 20 (3, 9, 8,)
    print(max_sum(array, 3))

    # Find the max average:
    array = [1, 0, 3, 5, 1, 3, 9, 6, 1, 2]  # (6, [3, 9, 6])
    print(max_average(array, 3))
