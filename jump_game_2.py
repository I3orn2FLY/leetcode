class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        cur_i = 0
        jump_count = 0
        while cur_i < len(nums) - 1:
            jump_count += 1
            if cur_i + nums[cur_i] >= len(nums) - 1:
                break
            max_idx = cur_i
            next_i = cur_i
            for j in range(cur_i + 1, min(cur_i + nums[cur_i] + 1, len(nums))):
                if max_idx < j + nums[j]:
                    max_idx = j + nums[j]
                    next_i = j

            cur_i = next_i

        return jump_count



s = Solution()
# nums = [3, 2, 1]
nums = [2, 3, 1, 1, 4]
print(s.jump(nums))
