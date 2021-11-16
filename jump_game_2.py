class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0


        los = [0]
        mss = [0]
        for i in range(1, len(nums)):
            ms = float("inf")
            for j in range(i):
                diff = j + los[j] - i
                if diff < 0:
                    # cannot be reached from that index
                    continue
                if mss[j] < ms:
                    ms = mss[j]
            lo = -1
            for j in range(i):
                diff = j + los[j] - i
                if diff < 0:
                    # cannot be reached from that index
                    continue
                if mss[j] == ms:
                    lo = max(diff, lo)
            if lo >= 0:
                mss.append(ms)
                los.append(lo)
                # this index can be reached by someones leftovers
                continue

            # this index cannot be reached by someones leftovers:
            for j in range(i):
                diff = j + nums[j] - i
                if diff < 0:
                    # cannot be reached after taking step from j index
                    continue
                # can be reached after taking step from j index
                if mss[j] + 1 < ms:
                    ms = mss[j] + 1

            lo = -1
            for j in range(i):
                diff = j + nums[j] - i
                if diff < 0:
                    # cannot be reached after taking step from j index
                    continue
                # can be reached after taking step from j index
                if mss[j] + 1 == ms:
                    lo = max(diff, lo)

            mss.append(ms)
            los.append(lo)


        return mss[-1]


s = Solution()
nums = [2,3,0,1,4]
# nums = [2, 3, 1, 1, 4]
print(s.jump(nums))