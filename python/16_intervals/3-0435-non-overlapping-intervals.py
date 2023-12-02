from typing import List
import math


END = 1
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[END])
        count = 0
        limit = -math.inf
        
        for start, end in intervals:
            if start < limit:
                count += 1
            else:
                limit = end
        
        return count
