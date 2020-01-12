def BFS(matrix, queue, visited, m, n):
    while queue:
        i, j = queue.pop(0)
        if i > 0:
            y, x = i - 1, j
            if not visited[y][x] and matrix[i][j] <= matrix[y][x]:
                queue.append([y, x])
                visited[y][x] = True

        if j > 0:
            y, x = i, j - 1
            if not visited[y][x] and matrix[i][j] <= matrix[y][x]:
                queue.append([y, x])
                visited[y][x] = True

        if i < m - 1:
            y, x = i + 1, j
            if not visited[y][x] and matrix[i][j] <= matrix[y][x]:
                queue.append([y, x])
                visited[y][x] = True

        if j < n - 1:
            y, x = i, j + 1
            if not visited[y][x] and matrix[i][j] <= matrix[y][x]:
                queue.append([y, x])
                visited[y][x] = True


class Solution:
    def pacificAtlantic(self, matrix):

        if len(matrix) < 2:
            return [[i, j] for i in range(len(matrix)) for j in range(len(matrix[0]))]

        m = len(matrix)
        n = len(matrix[0])

        p_queue = [[i, 0] for i in range(m)] + [[0, j] for j in range(1, n)]
        a_queue = [[i, n - 1] for i in range(m)] + [[m - 1, j] for j in range(n - 1)]

        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]

        for i in range(m):
            p_visited[i][0] = True

        for i in range(n):
            p_visited[0][i] = True

        for i in range(n):
            a_visited[m - 1][i] = True

        for i in range(m):
            a_visited[i][n - 1] = True

        BFS(matrix, p_queue, p_visited, m, n)
        BFS(matrix, a_queue, a_visited, m, n)

        res = []
        for i in range(m):
            for j in range(n):
                if a_visited[i][j] and p_visited[i][j]:
                    res.append([i, j])

        return res


s = Solution()

res = s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])

print(res)
