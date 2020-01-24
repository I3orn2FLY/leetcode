def idx(char):
    return ord(char) - ord('a')


def dfs(board, trie, i, j, res):
    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] == '#':
        return

    trie = trie.children[idx(board[i][j])]
    if trie is None:
        return

    if trie.word:
        res.append(trie.word)
        trie.word = None

    tmp = board[i][j]

    board[i][j] = '#'

    dfs(board, trie, i + 1, j, res)
    dfs(board, trie, i - 1, j, res)
    dfs(board, trie, i, j + 1, res)
    dfs(board, trie, i, j - 1, res)

    board[i][j] = tmp


class Trie():
    def __init__(self, word=None):
        self.children = [None] * 26
        self.word = word

    def __repr__(self):
        return ""


def build_trie(words):
    root = Trie()
    for word in words:
        trie = root
        for c in word:
            i = idx(c)
            if trie.children[i] is None:
                trie.children[i] = Trie()

            trie = trie.children[i]

        trie.word = word

    return root


class Solution:

    def findWords(self, board, words):
        if not board or not board[0]:
            return []

        m = len(board)
        n = len(board[0])

        res = []

        root = build_trie(words)

        for i in range(m):
            for j in range(n):
                dfs(board, root, i, j, res)

        return res


s = Solution()

res = s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                  ["oath", "pea", "eat", "rain"])
print(res)
