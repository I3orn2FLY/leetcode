# Incorrect solution, proper solution is too hard
def get_med(nums):
    half = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[half - 1] + nums[half]) // 2, half, True
    else:
        return nums[half], half, False


# nums1 > nums2 by elements
def get_med_two_array_uncrossed(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    if n == m: return (nums1[0] + nums2[-1]) / 2

    if m > n:
        half = (n + m) // 2
        if (n + m) % 2 == 0:
            return (nums2[half - 1] + nums2[half]) // 2
        else:
            return nums2[half]

    if n > m:
        half = (n + m) // 2 - m
        if (n + m) % 2 == 0:
            return (nums1[half - 1] + nums1[half]) // 2
        else:
            return nums1[half]


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if not nums1: return get_med(nums2)[0]
        if not nums2: return get_med(nums1)[0]
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2

        if nums1[0] > nums2[-1]: return get_med_two_array_uncrossed(nums1, nums2)
        if nums2[0] > nums1[-1]: return get_med_two_array_uncrossed(nums2, nums1)

        med1, med1_idx, iseven1 = get_med(nums1)
        med2, med2_idx, iseven2 = get_med(nums2)

        if med1 > med2:
            nums1 = nums1[:med1_idx] if iseven1 else nums1[:med1_idx + 1]
            nums2 = nums2[med2_idx:]
        else:
            nums1 = nums1[med1_idx:]
            nums2 = nums2[:med2_idx] if iseven2 else nums2[:med2_idx + 1]

        return self.findMedianSortedArrays(nums1, nums2)


if __name__ == "__main__":
    s = Solution()

    print(s.findMedianSortedArrays([1, 3], [2]))
