from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * n for i in range(m)]

        def get_max_side(i, j):
            if dp[i][j] != -1:
                return
            if i == 0 or j == 0:
                dp[i][j] = 1 if matrix[i][j] == "1" else 0
            else:
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    get_max_side(i - 1, j)
                    get_max_side(i, j - 1)
                    get_max_side(i - 1, j - 1)
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        max_side = 0
        for i in range(m):
            for j in range(n):
                get_max_side(i, j)
                max_side = max(max_side, dp[i][j])
        return max_side * max_side


s = Solution()
print(s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
