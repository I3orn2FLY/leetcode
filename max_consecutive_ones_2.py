from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(len(nums), 1 + sum(nums))

        max_count = 0
        cur_count = 0
        connected_count = 0

        for i in range(len(nums)):
            if nums[i]:
                cur_count += 1
                connected_count += 1

            max_count = max(connected_count, max_count)

            if not nums[i]:
                cur_count = 0
                if i == 0 or not nums[i - 1]:
                    connected_count = 1
                elif nums[i - 1]:
                    connected_count += 1

        return max_count


s = Solution()
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
