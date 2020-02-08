class Solution:

    def bfs(self, matrix, i, j, res):
        if matrix[i][j] == '0':
            return 0

        if min(len(matrix) - i, len(matrix[0]) - j) <= res:
            return res

        size = 1
        while i + size < len(matrix) and j + size < len(matrix[0]):
            broken = False
            for k in range(size):
                if matrix[i + k][j + size] == '0':
                    broken = True
                    break
            for l in range(size + 1):
                if matrix[i + size][j + l] == '0':
                    broken = True
                    break

            if broken:
                break

            size += 1

        return size

    def maximalSquare(self, matrix) -> int:
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.bfs(matrix, i, j, res))

        return res * res


s = Solution()
print(s.maximalSquare([["0", "0", "0", "1"],
                       ["1", "1", "0", "1"],
                       ["1", "1", "1", "1"],
                       ["0", "1", "1", "1"],
                       ["0", "1", "1", "1"]]))
