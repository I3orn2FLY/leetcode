def get_med(nums):
    half = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[half - 1] + nums[half]) // 2, True
    else:
        return nums[half], False


# nums1 > nums2 by elements
def get_med_two_array_uncrossed(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    if n == m: return (nums1[0] + nums2[-1]) / 2

    if m > n:
        half = (n + m) / 2
        if (n + m) % 2 == 0:
            return (nums2[half - 1] + nums2[half]) // 2
        else:
            return nums2[half]

    if n > m:
        half = (n + m) / 2 - m
        if (n + m) % 2 == 0:
            return (nums1[half - 1] + nums1[half]) // 2
        else:
            return nums1[half]



class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if not nums1: return get_med(nums2)[0]
        if not nums2: return get_med(nums1)[0]

        if nums1[0] > nums2[-1]: return get_med_two_array_uncrossed(nums1, nums2)
        if nums2[0] > nums1[-1]: return get_med_two_array_uncrossed(nums2, nums1)

        med1, even = get_med(nums1)
        med2, even = get_med(nums2)

        # min_half =
        print(med1, even)
        print(med2, even)

        return med1


if __name__ == "__main__":
    s = Solution()

    s.findMedianSortedArrays([], [])
