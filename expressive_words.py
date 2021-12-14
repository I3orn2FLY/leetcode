from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def get_char_group(word: str) -> [[str, int]]:
            char_group = [[word[0], 1]]
            for char in word[1:]:
                if char == char_group[-1][0]:
                    char_group[-1][1] += 1
                else:
                    char_group.append([char, 1])

            return char_group

        def can_be_streched(src: str, dst: str) -> bool:
            char_group_src = get_char_group(src)
            char_group_dst = get_char_group(dst)

            if len(char_group_src) != len(char_group_dst):
                return False

            for i in range(len(char_group_src)):
                if char_group_src[i][0] != char_group_dst[i][0]:
                    return False

                count_src = char_group_src[i][1]
                count_dst = char_group_dst[i][1]
                if count_dst != count_src and (count_dst < count_src or count_dst < 3):
                    return False

            return True

        res = 0
        for word in words:
            if can_be_streched(word, s):
                res += 1

        return res


s = Solution()
print(s.expressiveWords("heeelllooo", ["hello", "hi", "helo", "hhhhhhhhhelo"]))
print(s.expressiveWords("heeellooo", ["hello", "hi", "helo", "hhhhhhhhhelo"]))
print(s.expressiveWords("zzzzzyyyyy", ["zzyy","zy","zyy"]))
