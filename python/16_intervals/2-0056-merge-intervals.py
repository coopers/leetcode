from typing import List


START, END = 0, 1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for s, e in intervals[1:]:
            if s <= res[-1][END]:
                res[-1][END] = max(res[-1][END], e)
            else:
                res.append([s, e])
        return res
