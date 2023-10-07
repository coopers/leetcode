from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            a, b = b, max(n + a, b)
        
        return b