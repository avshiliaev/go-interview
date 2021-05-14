# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for x in range(n + 1)]
        return self.climbStairs_recursive(dp, n)

    def climbStairs_recursive(self, dp, n):
        # we don't take any steps, so there is only 1 way
        if n == 0:
            return 0
        # we can take one step to reach the end, and this is the only way
        if n == 1:
            return 1
        # we can take one step twice or take two steps to reach the end
        if n == 2:
            return 2

        if dp[n] == 0:
            # if we take one step, we are left with "n - 1" steps
            take1step = self.climbStairs_recursive(dp, n - 1)
            # if we take two steps, we are left with "n - 2" steps
            take2steps = self.climbStairs_recursive(dp, n - 2)

            dp[n] = take1step + take2steps

        return dp[n]
