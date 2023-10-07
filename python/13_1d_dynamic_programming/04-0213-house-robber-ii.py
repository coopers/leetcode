from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        def helper(nums):
            a, b = 0, 0
            for n in nums:
                a, b = b, max(n + a, b)
            
            return b

        return max(helper(nums[:-1]), helper(nums[1:]))
