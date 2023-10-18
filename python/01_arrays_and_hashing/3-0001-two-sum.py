from typing import List



# Time   O(N)
# Space  O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in m:
                return [i, m[complement]]
            
            m[n] = i
