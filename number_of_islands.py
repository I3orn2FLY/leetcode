class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, m, n)
                    count += 1
        return count

    def bfs_step(self, queue, grid, y, x):
        if grid[y][x] == '1':
            queue.append([y, x])
            grid[y][x] == '0'

    def bfs(self, grid, i, j, m, n):
        queue = [[i, j]]
        grid[i][j] = '0'
        while queue:
            i, j = queue.pop(0)
            if i > 0:
                self.bfs_step(queue, grid, i - 1, j)

            if j > 0:
                self.bfs_step(queue, grid, i, j - 1)

            if i < m - 1:
                self.bfs_step(queue, grid, i + 1, j)

            if j < n - 1:
                self.bfs_step(queue, grid, i, j + 1)