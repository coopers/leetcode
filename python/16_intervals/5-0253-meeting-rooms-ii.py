from typing import List


START, END = 0, 1
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted([i[START] for i in intervals])
        end_times = sorted(i[END] for i in intervals)
        rooms = 0
        i = 0
        for start_time in start_times:
            if start_time >= end_times[i]:
                i += 1
            else:
                rooms += 1

        return rooms