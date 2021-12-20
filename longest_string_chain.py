from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        G = {i: set() for i in range(len(words))}
        words.sort(key=lambda x: len(x))

        def isPredecessor(word, later_word):
            used = 0
            for i in range(len(later_word)):
                if i == len(later_word) - 1 and not used:
                    return True
                if later_word[i] != word[i - used]:
                    used += 1
                    if used > 1:
                        return False

            return True

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[j]) == len(words[i]):
                    continue
                if len(words[j]) - len(words[i]) > 1:
                    break
                if isPredecessor(words[i], words[j]):
                    G[i].add(j)

        distances = {i: 0 for i in range(len(words))}

        def get_distance(node):
            if distances[node] == 0:
                if not G[node]:
                    distances[node] = 1
                else:
                    res = 0
                    for neighbor in G[node]:
                        res = max(res, 1 + get_distance(neighbor))

                    distances[node] = res

            return distances[node]
        res = 1
        for i in range(len(words)):
            res = max(get_distance(i), res)

        return res


s = Solution()

print(s.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(s.longestStrChain(["abcd","dbqca"]))
