class Solution:
    def findAnagrams(self, s: str, p: str):
                                        if len(p) > len(s):
                                            return []

                                        p_dict = dict()

                                        for ch in p:
                                            p_dict[ch] = p_dict.get(ch, 0) + 1

                                        res = []
                                        L = len(p)
                                        word = dict()
                                        i = -1
                                        for j, ch in enumerate(s):
                                            p_c = p_dict.get(ch, 0)

                                            if p_c == 0:
                                                i = j
                                                word = dict()
                                                continue

                                            w_c = word.get(ch, 0)

                                            if w_c == p_c:
                                                for i in range(i + 1, j):
                                                    word[s[i]] -= 1

                                                    if s[i] == ch:
                                                        break

                                            word[ch] = word.get(ch, 0) + 1

                                            if j - i == L:
                                                res.append(i + 1)
                                                i += 1
                                                word[s[i]] -= 1

                                        return res


s = Solution()

print(s.findAnagrams("abaacbabc", "abc"))
