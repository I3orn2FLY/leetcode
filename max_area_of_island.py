from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        m = len(grid)
        n = len(grid[0])

        def get_area(i, j):
            if grid[i][j] != 1:
                return 0
            res = 1

            grid[i][j] = 0
            for y, x in offsets:
                y, x = i + y, j + x
                if 0 <= x < n and 0 <= y < m and grid[y][x] == 1:
                    res += get_area(y, x)

            return res

        max_area = 0
        for i in range(m):
            for j in range(n):
                max_area = max(max_area, get_area(i, j))

        return max_area


s = Solution()

print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
