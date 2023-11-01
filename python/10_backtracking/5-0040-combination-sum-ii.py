from typing import List



class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(chosen, remaining, diff):
            if not diff:
                res.append(chosen)
            elif remaining:
                if remaining[0] > diff:
                    return
                helper(chosen + [remaining[0]], remaining[1:], diff - remaining[0])
                i = 1
                while i < len(remaining) and remaining[i] == remaining[i - 1]:
                    i += 1
                helper(chosen, remaining[i:], diff)

        helper([], nums, target)
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(chosen, remaining, diff):
            if not diff:
                res.append(chosen)
            elif diff > 0 and remaining:
                i = 1
                backtrack(chosen + [remaining[0]], remaining[i:], diff - remaining[0])
                while i < len(remaining) and remaining[i] == remaining[i - 1]:
                    i += 1
                backtrack(chosen, remaining[i:], diff)

        backtrack([], candidates, target)
        return res
    

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(chosen, i, diff):
            if not diff:
                res.append(chosen)
            elif diff > 0 and i < len(candidates):
                backtrack(chosen + [candidates[i]], i + 1, diff - candidates[i])
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                backtrack(chosen, i + 1, diff)

        backtrack([], 0, target)
        return res
    


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(cur, index, target):
            if target == 0:
                res.append(cur.copy())

            elif target > 0:
                prev = -1
                for i, num in enumerate(candidates[index:]):
                    if num != prev:
                        cur.append(num)
                        backtrack(cur, index + i + 1, target - num)
                        prev = cur.pop()

        backtrack([], 0, target)
        return res