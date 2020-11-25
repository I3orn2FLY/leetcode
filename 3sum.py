class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            r = len(nums) - 1
            l = i + 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif total < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1

        return res


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))

s = Solution()

print(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
