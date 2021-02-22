class Solution:

    def contain(self, s, words):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for j in range(i):
                if not dp[j]: continue
                if s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]

    def findAllConcatenatedWordsInADict(self, words):
        words.sort(key=lambda w: -len(w))
        words_set = set(words)

        res = []
        for i in range(len(words) - 1):
            s = words[i]
            words_set.remove(s)
            if self.contain(s, words_set):
                res.append(s)

        return res


s = Solution()
print(s.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
