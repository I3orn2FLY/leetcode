class Solution(object):
    def canJump(self, nums) -> bool:
        if len(nums) <= 1:
            return True
        elif nums[0] == 0:
            return False

        max_steps = nums[0]
        for i in range(1, len(nums) - 1):
            max_steps = max(nums[i], max_steps - 1)
            if max_steps < 1:
                return False

        return True


s = Solution()
nums = [3, 2, 1, 0, 4]
# nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))
