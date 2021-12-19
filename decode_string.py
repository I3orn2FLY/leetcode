class Solution:
    def decodeString(self, s: str) -> str:

        i = 0
        res = []
        while i < len(s):

            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1

                count = int(s[i:j])

                i = j + 1
                bracket_count = 1
                while bracket_count:
                    j += 1
                    if s[j] == "]":
                        bracket_count -= 1
                    elif s[j] == "[":
                        bracket_count += 1

                res += [self.decodeString(s[i:j])] * count
                i = j + 1

            else:
                res.append(s[i])
                i += 1

        return "".join(res)


s = Solution()

print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString("abc3[cd]xyz"))