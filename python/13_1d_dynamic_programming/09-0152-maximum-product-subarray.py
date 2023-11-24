from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = lil = big = nums[0]
        for c in nums[1:]:
            l, b = lil * c, big * c
            lil = min(l, b, c)
            big = max(l, b, c)
            res = max(res, big)

        return res
