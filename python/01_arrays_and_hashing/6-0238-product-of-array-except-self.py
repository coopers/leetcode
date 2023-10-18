from typing import List



# Time   O(N)
# Space  O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for n in nums:
            res.append(prefix)
            prefix *= n

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res