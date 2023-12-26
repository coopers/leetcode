from typing import List



# N: number of candidates
# T: target value
# M: min value of candidates
# Depth of the tree: T/M

# Time:  O(N^(T/M + 1))
# Space: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(chosen, remaining, diff):
            if not diff:
                res.append(chosen)
            elif remaining and diff > 0:
                helper(chosen + [remaining[0]], remaining, diff - remaining[0])
                helper(chosen, remaining[1:], diff)

        helper([], candidates, target)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        chosen = []
        def helper(i, diff):
            if not diff:
                res.append(chosen[:])
            elif i < len(candidates) and diff > 0:
                chosen.append(candidates[i])
                helper(i, diff - candidates[i])
                chosen.pop()
                helper(i+1, diff)
        
        helper(0, target)
        return res