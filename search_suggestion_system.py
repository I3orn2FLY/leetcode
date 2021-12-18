from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []

        products.sort()

        s = 0
        e = len(products)
        while len(res) < len(searchWord):
            j = len(res)
            char = searchWord[j]
            while s < e and (len(products[s]) - 1 < j or products[s][j] < char):
                s += 1

            while e > s and (len(products[e - 1]) - 1 < j or products[e - 1][j] > char):
                e -= 1

            if s >= e:
                res.append([])
            else:
                res.append(products[s: min(s + 3, e)])

        return res


s = Solution()

print(s.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "bags"))
