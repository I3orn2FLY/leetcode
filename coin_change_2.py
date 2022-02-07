from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[-1] * len(coins) for _ in range(amount + 1)]

        dp[0] = [1] * len(coins)

        def get_ways(t, i):
            if t < 0:
                return 0

            if dp[t][i] == -1:
                res = 0
                for j in range(i, len(coins)):
                    ways = get_ways(t - coins[j], j)
                    res += ways

                dp[t][i] = res

            return dp[t][i]


        get_ways(amount, 0)
        return dp[amount][0]


s = Solution()
print(s.change(5, [1, 2, 5]))
