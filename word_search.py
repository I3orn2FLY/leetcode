def dfs(board, i, j, word, idx):
    if idx == len(word):
        return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[idx] != board[i][j]:
        return False

    c = board[i][j]
    board[i][j] = '#'

    res = dfs(board, i - 1, j, word, idx + 1) \
          or dfs(board, i, j - 1, word, idx + 1) \
          or dfs(board, i + 1, j, word, idx + 1) \
          or dfs(board, i, j + 1, word, idx + 1)

    board[i][j] = word[idx]

    return res


class Solution:
    def exist(self, board, word: str) -> bool:
        if not board: return False
        if not board[0]: return False
        if not word: return False
        print("HELLO")
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word, 0):
                    return True

        return False

s = Solution()

ans = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
print(ans)