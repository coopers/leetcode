from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(chosen, remaining):
            if not remaining:
                res.append(chosen)
            else:
                helper(chosen + [remaining[0]], remaining[1:] )
                helper(chosen, remaining[1:])

        helper([], nums)
        return res