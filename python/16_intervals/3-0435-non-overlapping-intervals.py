from typing import List
import math


END = 1
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[END])
        ans = 0
        k = -math.inf
        
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1
        
        return ans
