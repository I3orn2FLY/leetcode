from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G = dict()
        G_rev = dict()
        max_len = 0
        for word in words:
            max_len = max(len(word), max_len)
            for ch in word:
                G[ch] = G.get(ch, set())
                G_rev[ch] = G_rev.get(ch, set())

        for j in range(max_len):
            for i in range(1, len(words)):
                prev_word = words[i - 1]
                cur_word = words[i]
                if j == len(cur_word) and len(prev_word) > j and cur_word == prev_word[:j]:
                    return ""
                if j >= len(cur_word) or j >= len(prev_word):
                    continue
                prev_char = prev_word[j]
                cur_char = cur_word[j]
                if prev_word[:j] == cur_word[:j] and prev_char != cur_char:
                    G[prev_char].add(cur_char)
                    G_rev[cur_char].add(prev_char)

        status = {node: 0 for node in G}

        # 0 not checked
        # 1 being checked
        # 2 checked and no cycle
        # 3 checked and cycle

        def get_cycle_status(node):
            if status[node] == 1:
                status[node] = 3
            elif status[node] == 0:
                status[node] = 1
                for neighbor in G[node]:
                    get_cycle_status(neighbor)
                    if status[neighbor] == 3:
                        status[node] = 3
                        return
                status[node] = 2

        for node in G:
            get_cycle_status(node)
            if status[node] == 3:
                return ""

        res = []

        while G:
            level = [node for node in G if not G_rev[node]]
            for node in level:
                if not G_rev[node]:
                    res.append(node)
                    for neighbor in G[node]:
                        G_rev[neighbor].remove(node)
                    del G[node]

        return "".join(res)


s = Solution()
print(s.alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]))

print(s.alienOrder([
    "z", "x", "z"
]))
print(s.alienOrder([
    "z", "x"
]))
