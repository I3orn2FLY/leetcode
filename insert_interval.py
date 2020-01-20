class Solution:
    def insert(self, intervals, newInterval):
        # intervals.sort(key=lambda x: x[0])
        if not intervals:
            return [newInterval]

        start = newInterval[0]
        end = newInterval[1]
        right = left = 0
        while right < len(intervals):
            if start <= intervals[right][1]:
                if end < intervals[right][0]:
                    break
                start = min(start, intervals[right][0])
                end = max(end, intervals[right][1])
            else:
                left += 1
            right += 1
        return intervals[:left] + [[start, end]] + intervals[right:]


s = Solution()

# res = s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
res = s.insert([[1, 5]], [5, 7])

print(res)
