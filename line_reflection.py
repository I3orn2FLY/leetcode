from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if len(points) < 2:
            return True

        points.sort()

        i = 0
        j = len(points) - 1

        mid = (points[0][0] + points[-1][0]) / 2

        while i <= j:
            if (points[i][0] + points[j][0]) / 2 != mid:
                return False

            if points[i][0] == points[j][0]:
                break

            k = i
            while points[k][0] == points[k + 1][0]:
                k += 1

            l = j
            while points[l][0] == points[l - 1][0]:
                l -= 1

            new_j = l - 1

            while i <= k and l <= j:
                if points[i][1] != points[l][1]:
                    return False

                i += 1
                while i <= k and points[i][1] == points[i - 1][1]:
                    i += 1

                l += 1
                while l <= j and points[l][1] == points[l - 1][1]:
                    l += 1

            j = new_j
        return True


s = Solution()
# print(s.isReflected([[0, 0], [1, 0], [3, 0]]))
print(s.isReflected([[1, 2], [2, 2], [1, 4], [2, 4]]))
