from typing import List


# incorrect solution, time limit exceeded

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        full_area = 0
        xmin, ymin, xmax, ymax = None, None, None, None
        for x0, y0, x1, y1 in rectangles:
            if xmin is None or x0 < xmin:
                xmin = x0

            if ymin is None or y0 < ymin:
                ymin = y0

            if xmax is None or x1 > xmax:
                xmax = x1

            if ymax is None or y1 > ymax:
                ymax = y1

            full_area += (x0 - x1) * (y0 - y1)

        if (xmin - xmax) * (ymin - ymax) != full_area:
            return False

        def get_inter(box1, box2):
            x0 = max(box1[0], box2[0])
            y0 = max(box1[1], box2[1])
            x1 = min(box1[2], box2[2])
            y1 = min(box1[3], box2[3])

            if x0 >= x1 or y0 >= y1:
                return 0
            else:
                return 1

        for i in range(len(rectangles) - 1):
            for j in range(i + 1, len(rectangles)):

                interception = get_inter(rectangles[i], rectangles[j])

                if interception:
                    return False

        return True


s = Solution()
print(s.isRectangleCover(
    [[0, 0, 4, 1], [7, 0, 8, 2], [6, 2, 8, 3], [5, 1, 6, 3], [4, 0, 5, 1], [6, 0, 7, 2], [4, 2, 5, 3], [2, 1, 4, 3],
     [0, 1, 2, 2], [0, 2, 2, 3], [4, 1, 5, 2], [5, 0, 6, 1]]))

print(s.isRectangleCover([[0, 0, 1, 1], [0, 1, 3, 2], [1, 0, 2, 2]]))
