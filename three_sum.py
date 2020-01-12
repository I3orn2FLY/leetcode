# Sorting
def threeSum(nums):
    ans = []
    nums.sort()
    L = len(nums)
    for idx in range(L - 2):

        if nums[idx] > 0:
            break

        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue

        l = idx + 1
        r = L - 1
        while (l < r):

            total = nums[l] + nums[r] + nums[idx]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                ans.append([nums[idx], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]))
