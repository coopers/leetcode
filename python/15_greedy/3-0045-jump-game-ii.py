from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        prev, curr = 0, 0
        
        for i in range(n - 1):
            curr = max(curr, i + nums[i])
            if i == prev:
                res += 1
                prev = curr
                
        return res
