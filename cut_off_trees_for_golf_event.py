from typing import List
from collections import deque
import heapq


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        heap = []

        m = len(forest)
        n = len(forest[0])

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heap.append([forest[i][j], (i, j)])

        heapq.heapify(heap)

        def get_neighbors(i, j):
            res = []
            if i > 0:
                res.append((i - 1, j))

            if i < m - 1:
                res.append((i + 1, j))

            if j > 0:
                res.append((i, j - 1))

            if j < n - 1:
                res.append((i, j + 1))

            return res

        def get_steps(s, e):

            queue = deque([s])
            distance = {s: 0}

            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()

                    if e == (i, j):
                        return distance[e]

                    for x, y in get_neighbors(i, j):
                        if (x, y) in distance or forest[x][y] == 0:
                            continue

                        queue.append((x, y))
                        distance[(x, y)] = distance[(i, j)] + 1

            return -1

        s = (0, 0)
        res = 0
        while heap:
            h, e = heapq.heappop(heap)
            d = get_steps(s, e)
            if d == -1:
                return -1

            res += d

            s = e

        return res


s = Solution()
print(s.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
