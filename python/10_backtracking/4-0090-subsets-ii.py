from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(chosen, remaining):
            if not remaining:
                res.append(chosen)
            else:
                i = 1
                helper(chosen + [remaining[0]], remaining[i:])
                while i < len(remaining) and remaining[i] == remaining[i - 1]:
                    i += 1 
                helper(chosen, remaining[i:])

        helper([], nums)
        return res