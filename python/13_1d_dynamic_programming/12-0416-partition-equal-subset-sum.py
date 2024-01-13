from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half, is_odd = divmod(sum(nums), 2)
        if is_odd:
            return False
        
        sums = {0}
        for n in nums:
            sums |= {n + s for s in sums}
            if half in sums:
                return True

        return False
