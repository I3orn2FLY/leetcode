def initialize(intervals, start_idx):
    s_prev, e_prev = intervals[start_idx]
    return e_prev, e_prev - s_prev, start_idx, start_idx


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort(key=lambda x: x[0])

        start_idx = 0
        rm = 0
        e_prev, max_width, idx, del_idx = initialize(intervals, start_idx)
        idx += 1
        while (idx < len(intervals)):
            s_cur, e_cur = intervals[idx]
            if s_cur < e_prev:
                width = e_prev - s_cur
                if width > max_width:
                    max_width = width
                    del_idx = idx
            elif idx - start_idx > 1:
                del intervals[del_idx]
                rm += 1
                e_cur, max_width, idx, del_idx = initialize(intervals, start_idx)
            else:
                start_idx, del_idx = idx, idx
                max_width = e_cur - s_cur

            if idx == len(intervals) - 1 and s_cur < e_prev:
                del intervals[del_idx]
                rm += 1
                e_cur, max_width, idx, del_idx = initialize(intervals, start_idx)

            e_prev = e_cur
            idx += 1

        return rm


s = Solution()

# res = s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
res = s.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]])

print(res)
