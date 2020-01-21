class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        is_pal = [[False] * len(s) for _ in range(len(s))]

        is_pal[0][0] = True
        res = s[0]
        for d in range(1, len(s)):

            i = j = d
            is_pal[i][j] = True

            while i > 0 and j < len(s) - 1:
                i = i - 1
                j = j + 1

                if s[i] == s[j]:
                    is_pal[i][j] = is_pal[i + 1][j - 1]
                else:
                    is_pal[i][j] = False

                if is_pal[i][j] and (j - i + 1) > len(res):
                    res = s[i:j + 1]

            i, j = d, d - 1
            is_pal[i][j] = s[i] == s[j]

            while i > 0 and j < len(s) - 1:
                i = i - 1
                j = j + 1

                if s[i] == s[j]:
                    is_pal[i][j] = is_pal[i + 1][j - 1]
                else:
                    is_pal[i][j] = False

                if is_pal[i][j] and (j - i + 1) > len(res):
                    res = s[i:j + 1]

        return res


s = Solution()

s.longestPalindrome("babad")
