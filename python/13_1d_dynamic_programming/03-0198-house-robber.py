from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for nxt in nums:
            prev, curr = curr, max(prev + nxt, curr)
        
        return curr
