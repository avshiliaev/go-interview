class Solution:
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


if __name__ == '__main__':
    array = [4, 5, 1, 7, 4, 9, 2, 3, 1, 0, -1, 8, 6, -4]
    new_array = Solution().sort(array)
    print(new_array)
