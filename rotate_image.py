class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for s in range(len(matrix) // 2):
            for k in range(s, len(matrix) - s - 1):
                i, j = s, k
                tmp = matrix[i][j]
                for _ in range(4):
                    m, n = j, len(matrix) - i - 1
                    matrix[m][n], tmp = tmp, matrix[m][n]
                    i, j = m, n


s = Solution()

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(A)

print(A)

A = [[5, 1, 9, 11],
     [2, 4, 8, 10],
     [13, 3, 6, 7],
     [15, 14, 12, 16]
     ],

print(A)