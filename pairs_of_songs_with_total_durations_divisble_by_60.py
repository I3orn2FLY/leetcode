from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder2count = dict()

        for t in time:
            remainder = t % 60
            remainder2count[remainder] = remainder2count.get(remainder, 0) + 1

        n = 0
        for remainder in range(31):
            if remainder not in remainder2count:
                continue

            count = remainder2count[remainder]
            if remainder in {0, 30}:
                n += int(count * (count - 1) / 2)
            else:
                counter_count = remainder2count.get(60 - remainder, 0)

                n += count * counter_count


        return n

s = Solution()
print(s.numPairsDivisibleBy60([30,20,150,100,40]))