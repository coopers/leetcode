from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(chosen, remaining):
            if not remaining:
                res.append(chosen)
            else:
                for i in range(len(remaining)):
                    helper(chosen + [remaining[i]], remaining[:i] + remaining[i + 1:])

        helper([], nums)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        res = []
        for _ in range(len(nums)):
            n = nums.pop(0)
            res.extend([perm + [n] for perm in self.permute(nums)])
            nums.append(n)
        return res
