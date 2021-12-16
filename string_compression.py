from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        res = 0
        i = 0
        while i < len(chars):

            char = chars[i]
            count = 1
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            i += 1
            chars[res] = char
            res += 1
            if count > 1:
                for ch in str(count):
                    chars[res] = ch
                    res += 1
        return res


s = Solution()

print(s.compress(["a","a","b","b","c","e", "e","d"]))
