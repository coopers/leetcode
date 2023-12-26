from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        def helper(nums):
            prev, curr = 0, 0
            for nxt in nums:
                prev, curr = curr, max(nxt + prev, curr)
            
            return curr

        return max(helper(nums[:-1]), helper(nums[1:]))
