from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        sums = {0}
        for n in nums:
            additions = {n + s for s in sums}
            if target in additions:
                return True
            sums |= additions

        return False