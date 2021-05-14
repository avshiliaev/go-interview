from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        # initialize two-dimensional dp array, -1 for default
        dp = [[-1 for x in range(int(s / 2) + 1)] for y in range(len(nums))]

        if self.can_partition_recursive(dp, nums, int(s / 2), 0) == 1:
            return True  # return True for 1
        else:
            return False  # return False for 0

    def can_partition_recursive(self, dp, nums, sum, current_index):
        if sum == 0:
            return 1

        if len(nums) == 0 or current_index >= len(nums):
            return 0

        if dp[current_index][sum] == -1:  # if we have not processed this sub-problem
            if nums[current_index] <= sum:
                if self.can_partition_recursive(dp, nums, sum - nums[current_index], current_index + 1) == 1:
                    dp[current_index][sum] = 1
                    return 1

            # recursive call after excluding the number at the current_index
            dp[current_index][sum] = self.can_partition_recursive(dp, nums, sum, current_index + 1)

        return dp[current_index][sum]
