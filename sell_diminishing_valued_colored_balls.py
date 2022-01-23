from typing import List
from collections import Counter


class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        arr = sorted(Counter(inv).items(), reverse=True) + [(0, 0)]
        ans, ind, width = 0, 0, 0

        while orders > 0:
            width += arr[ind][1]
            sell = min(orders, width * (arr[ind][0] - arr[ind + 1][0]))
            whole, remainder = divmod(sell, width)
            ans += width * (whole * (arr[ind][0] + arr[ind][0] - (whole - 1))) // 2 + remainder * (arr[ind][0] - whole)
            orders -= sell
            ind += 1
        return ans % 1_000_000_007


s = Solution()

print(s.maxProfit([2, 2, 2, 5, 5, 5, 6, 6, 6, 7, 8, 9, 10], 50))
