from typing import List


START, END = 0, 1
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(
            intervals[i][END] <= intervals[i + 1][START]
            for i in range(len(intervals) - 1)
        )