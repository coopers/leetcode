from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        lil, big = 1, 1
        for n in nums:
            a, b = n * lil, n * big
            lil, big = min(a, b, n), max(a, b, n)
            res = max(res, big)

        return res
