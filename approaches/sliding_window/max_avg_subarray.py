# https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = []
        _sum, start = 0, 0
        for end in range(len(nums)):
            _sum += nums[end]  # add the next element

            if end >= k - 1:
                average.append(_sum / k)  # calculate the average
                _sum -= nums[start]  # subtract the element going out
                start += 1  # slide the window

        return max(average)
