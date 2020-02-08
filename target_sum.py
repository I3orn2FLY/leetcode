class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        memo = [[-1] * len(nums) for _ in range(2001)]

        def target_sum(t, j):
            if t == 0 and j == -1:
                return 1

            if j < 0 or j >= len(nums) or t < -1000 or t > 1000:
                return 0

            i = t + 1000

            if memo[i][j] > -1:
                return memo[i][j]

            n = target_sum(t - nums[j], j - 1) + target_sum(t + nums[j], j - 1)

            memo[i][j] = n

            return n

        return target_sum(S, len(nums) - 1)



s = Solution()
s.findTargetSumWays([1, 999], 998)
