from typing import List


class Trie:
    def __init__(self, is_word=False):
        self.nodes = dict()
        self.is_word = is_word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()

        for word in words:
            cur_trie = trie
            for i in range(len(word)):
                ch = word[i]
                if ch not in cur_trie.nodes:
                    cur_trie.nodes[ch] = Trie()
                cur_trie = cur_trie.nodes[ch]

            cur_trie.is_word = True

        m = len(board)
        n = len(board[0])

        res = []

        def dfs(i, j, trie, path):

            ch = board[i][j]
            if ch == "#" or ch not in trie.nodes:
                return

            path = path + ch
            trie = trie.nodes[ch]

            if trie.is_word:
                trie.is_word = False
                res.append(path)

            board[i][j] = "#"

            if i > 0:
                dfs(i - 1, j, trie, path)
            if i < m - 1:
                dfs(i + 1, j, trie, path)
            if j > 0:
                dfs(i, j - 1, trie, path)
            if j < n - 1:
                dfs(i, j + 1, trie, path)

            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")

        return res


s = Solution()

print(s.findWords([["a", "b"], ["a", "a"]],
                  ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]))
