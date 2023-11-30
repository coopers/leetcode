from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = res = 0
        while r < len(nums) - 1:
            res += 1
            l, r = r + 1, max(i + nums[i] for i in range(l, r + 1)) 
        return res
