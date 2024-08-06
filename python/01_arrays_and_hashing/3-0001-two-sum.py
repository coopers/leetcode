from typing import List


# Time   O(N)
# Space  O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementToIndex = {}
        for i, n in enumerate(nums):
            if n in complementToIndex:
                return [complementToIndex[n], i]
            
            complementToIndex[target - n] = i
