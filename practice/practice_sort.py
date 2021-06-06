class BubbleSort:
    def sort(self, arr):
        return arr


class MergeSort:
    """
    https://youtu.be/KF2j-9iSf4Q
    """

    def sort(self, arr):
        return self._merge_sort(arr)

    def _merge_sort(self, arr):

        # Base case for recursion:
        if len(arr) <= 2:
            return sorted(arr)

        result = []
        mid = len(arr) // 2
        left_arr = self._merge_sort(arr[:mid])
        right_arr = self._merge_sort(arr[mid:])

        return self._merge_halves(result, left_arr, right_arr)

    @staticmethod
    def _merge_halves(result, left_arr, right_arr):
        # Two pointers to iterate over two sub arrays:
        left, right = 0, 0
        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left] > right_arr[right]:
                result.append(right_arr[right])
                right += 1
            else:
                result.append(left_arr[left])
                left += 1

        # Take the rest:
        result += left_arr[left:]
        result += right_arr[right:]

        return result


class QuickSort:
    """
    https://youtu.be/SLauY6PpjW4
    https://stackoverflow.com/a/27461889/10202443
    """

    def sort(self, arr_):
        return self._quick_sort(arr_, 0, len(arr_) - 1)

    def _quick_sort(self, arr_, left, right):

        # Base case for recursion:
        if left >= right:
            return

        pivot = self._partition(arr_, left, right)
        self._quick_sort(arr_, left, pivot - 1)
        self._quick_sort(arr_, pivot + 1, right)

    @staticmethod
    def _partition(arr_, left, right):
        pivot = left
        for i in range(left + 1, right + 1):
            if arr_[i] <= arr_[left]:
                pivot += 1
                arr_[i], arr_[pivot] = arr_[pivot], arr_[i]
        arr_[pivot], arr_[left] = arr_[left], arr_[pivot]
        return pivot


if __name__ == '__main__':
    array = [4, 5, 1, 7, 4, 9, 2, 3, 1, 0, -1, 8, 6, -4]
    new_array = MergeSort().sort(array)
    print(new_array)

    array = [4, 5, 1, 7, 4, 9, 2, 3, 1, 0, -1, 8, 6, -4]
    QuickSort().sort(array)
    print(array)

    array = [4, 5, 1, 7, 4, 9, 2, 3, 1, 0, -1, 8, 6, -4]
    new_array = BubbleSort().sort(array)
    print(new_array)
