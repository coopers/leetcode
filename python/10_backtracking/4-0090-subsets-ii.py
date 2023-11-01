from typing import List


# Time:  O(N ✖️ 2^N)
# Space: O(log(N))
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
    

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res