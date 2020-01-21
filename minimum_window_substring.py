class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        cur_word_count = {c: 0 for c in t}
        req_word_count = {c: 0 for c in t}
        for ch in t:
            req_word_count[ch] += 1

        cur_len_word = 0
        req_len_word = sum(req_word_count[ch] for ch in req_word_count)
        res_word = ""
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in req_word_count:
                j += 1
                continue

            if i != j and s[i] not in req_word_count:
                i += 1
                continue

            if i != j and cur_word_count[s[i]] > req_word_count[s[i]]:
                cur_word_count[s[i]] -= 1
                i += 1
                continue

            if cur_word_count[s[j]] < req_word_count[s[j]]:
                cur_len_word += 1

            cur_word_count[s[j]] += 1
            j += 1

            if cur_len_word == req_len_word:

                word_len = j - i
                if word_len == req_word_count:
                    return s[i:j]

                if not res_word or word_len < len(res_word):
                    res_word = s[i:j]

                cur_word_count[s[i]] -= 1
                i += 1
                cur_len_word -= 1

        return res_word


s = Solution()

res = s.minWindow("ADOBE16789CODEBA5NC", "615897")
print(res)
