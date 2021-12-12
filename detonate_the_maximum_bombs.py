from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        L = len(bombs)
        G = {i: set() for i in range(L)}

        for i in range(L):
            for j in range(L):
                if i == j:
                    continue

                x0, y0, r0 = bombs[i]
                x1, y1, r1 = bombs[j]

                dst = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

                if dst <= r0:
                    G[i].add(j)

        visited = set()

        def get_size(node):
            visited.add(node)
            size = 1
            for j in G[node]:
                if j not in visited:
                    size += get_size(j)
            return size

        res = 0
        for node in G:
            visited = set()

            res = max(get_size(node), res)

        return res


s = Solution()
# print(s.maximumDetonation([[2, 1, 3], [6, 1, 4]]))
print(s.maximumDetonation(
    [[868, 658, 84], [82, 386, 48], [464, 157, 11], [422, 654, 85], [864, 418, 84], [366, 314, 72], [955, 270, 60],
     [460, 98, 60], [824, 147, 38], [580, 660, 27], [423, 102, 73], [317, 471, 74]]))
