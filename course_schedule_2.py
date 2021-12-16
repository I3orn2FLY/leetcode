from typing import List
# topological sort should be done, and it is implemented with DFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = {i: set() for i in range(numCourses)}

        for edge in prerequisites:
            if edge[0] == edge[1]:
                return []
            G[edge[0]].add(edge[1])

        status = [0] * numCourses

        # 0 not visited
        # 1 in path
        # 2 visited, ok
        # 3 visited, cycle

        def get_status(i):
            if status[i] == 1:
                status[i] = 3

            if status[i] in {2, 3}:
                return

            status[i] = 1

            for j in G[i]:
                get_status(j)
                if status[j] == 3:
                    status[i] = 3
                    return

            status[i] = 2

        for i in range(numCourses):
            get_status(i)
            if status[i] == 3:
                return []

        res = []
        while G:
            for i in G:
                if G[i]: continue
                res.append(i)
                for j in G:
                    if i in G[j]:
                        G[j].remove(i)

        return res


s = Solution()

print(s.findOrder(4, [[0, 1], [0, 2], [2, 1], [3, 0], [2, 3]]))
