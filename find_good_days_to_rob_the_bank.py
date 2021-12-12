from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        L = len(security)
        if time > L // 2:
            return []

        if time == 0:
            return list(range(L))

        def calc_max_after(k, limit):
            max_after = 0
            for i in range(k + 1, min(k + limit + 1, len(security))):
                if security[i] < security[i - 1]:
                    break
                max_after += 1

            return max_after

        def calc_max_before(k, limit):
            max_before = 0
            for i in range(k, k - limit, -1):
                if security[i] > security[i - 1]:
                    break
                max_before += 1

            return max_before

        aft = calc_max_after(time, time)
        bf = calc_max_before(time, time)

        n = time

        res = []
        while n < L - time:
            while n < L - time and aft == bf == time:
                res.append(n)
                n += 1
                if security[n] > security[n - 1]:
                    bf = 0

                if n + time >= L or security[n + time] < security[n + time - 1]:
                    aft -= 1

            while n < L - time and not (time == bf == aft):
                jump = max(time - bf, max(aft, 1))
                n += jump
                pot_bf = calc_max_before(n, jump)
                if pot_bf == jump:
                    bf = min(bf + pot_bf, time)
                else:
                    bf = pot_bf

                aft = calc_max_after(n, time)
        return res


s = Solution()

print(s.goodDaysToRobBank([5, 3, 3, 3, 5, 6, 2], 2))
print(s.goodDaysToRobBank([1, 1, 1, 1, 1], 1))
print(s.goodDaysToRobBank([1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8], 2))
