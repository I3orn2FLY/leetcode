from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            G[edge[1]].append(edge[0])

        # 0 => not checked
        # 1 => being checked
        # 2 => checked and no cycle
        # 3 => checked and cycle

        status = [0] * numCourses

        def get_status(node):
            if status[node] == 0:  # not checked
                status[node] = 1  # being checked
                for neighbor in G[node]:

                    if status[neighbor] == 0:
                        get_status(neighbor)

                    if status[neighbor] in [1, 3]:
                        status[node] = 3
                        return status[node]
                status[node] = 2

            return status[node]

        for node in G:
            if status[node] == 0:
                if get_status(node) == 3:
                    return False

        return True


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
# print(s.canFinish(3, [[1, 0], [2, 1], [0, 2]]))
print(s.canFinish(4, [[0, 1], [3, 1], [1, 3], [3, 2]]))
