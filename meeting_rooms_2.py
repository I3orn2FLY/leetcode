from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 1
        end_times = [intervals[0][1]]
        for (start_time, end_time) in intervals[1:]:
            first_end_time = heapq.heappop(end_times)
            if start_time < first_end_time:
                rooms += 1
                heapq.heappush(end_times, first_end_time)

            heapq.heappush(end_times, end_time)

        return rooms