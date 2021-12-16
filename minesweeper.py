from typing import List
from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        m = len(board)
        n = len(board[0])

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        def get_neighbors(i, j):
            res = []
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if (k == i and l == j) or k < 0 or l < 0 or k > m - 1 or l > n - 1:
                        continue
                    res.append([k, l])

            return res

        queue = deque([click])
        while queue:
            L = len(queue)
            for _ in range(L):
                i, j = queue.popleft()

                if board[i][j] != "E":
                    continue

                bomb_count = 0
                neighbors = get_neighbors(i, j)
                for k, l in neighbors:
                    if board[k][l] == "M":
                        bomb_count += 1

                board[i][j] = str(bomb_count) if bomb_count else "B"
                if board[i][j] == "B":
                    for k, l in neighbors:
                        if board[k][l] == "E":
                            queue.append([k, l])
        return board


s = Solution()