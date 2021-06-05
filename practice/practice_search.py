def linear_search(arr_, k_):
    for i, v in enumerate(arr_):
        if v == k_:
            return i
    return -1


def binary_search(arr_, k_):
    mid = len(arr_) // 2
    while mid:
        if arr_[mid] == k_:
            return mid
        if k_ < arr_[mid]:
            arr_ = arr_[:mid]
        else:
            arr_ = arr_[mid:]
        mid = len(arr_) // 2
    return -1


if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7, 10, 14, 15, 21, 24, 35, 36]
    k = 6
    print(linear_search(arr, k))
    print(binary_search(arr, k))
