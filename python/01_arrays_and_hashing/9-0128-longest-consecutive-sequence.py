from typing import List


# Time   O(N)
# Space  O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for lo in s:
            if lo - 1 not in s:
                hi = lo + 1
                while hi in s:
                    hi += 1
         
                res = max(res, hi - lo)
        
        return res