from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        sums = {0}
        for n in nums:
            sums |= {n + s for s in sums}
            if target in sums:
                return True

        return False