from typing import List

START, END = 0, 1
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][END] < newInterval[START]:
                res.append(intervals[i])
            elif newInterval[END] < intervals[i][START]:
                return res + [newInterval] + intervals[i:]
            else:
                newInterval = [
                    min(newInterval[START], intervals[i][START]),
                    max(newInterval[END], intervals[i][END]),
                ]
        return res + [newInterval]


# Log Searching
START, END = 0, 1
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[END] < intervals[0][START]:
            return [newInterval] + intervals
        if newInterval[START] > intervals[-1][END]:
            return intervals + [newInterval]
        
        def getLower(n):
            res = -1
            l, r = 0, len(intervals) - 1
            while l <= r:
                m = l + (r - l) // 2
                if intervals[m][END] < n:
                    res = m
                    l = m + 1
                else:
                    r = m - 1
            return res + 1
        
        def getUpper(n):
            res = len(intervals)
            l, r = 0, len(intervals) - 1
            while l <= r:
                m = l + (r - l) // 2
                if intervals[m][START] > n:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            return res

        a, b = getLower(newInterval[START]), getUpper(newInterval[END])
        res = []
        if a:
            res.extend(intervals[:a])
        newInterval[START] = min(newInterval[START], intervals[a][START])
        newInterval[END] = max(newInterval[END], intervals[b-1][END])
        res.append(newInterval)
        if b != len(intervals):
            res.extend(intervals[b:])
        return res