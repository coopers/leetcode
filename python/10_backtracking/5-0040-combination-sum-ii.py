from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(chosen, remaining, diff):
            if not diff:
                res.append(chosen)
            if diff > 0 and remaining:
                i = 1
                backtrack(chosen + [remaining[0]], remaining[i:], diff - remaining[0])
                while i < len(remaining) and remaining[i] == remaining[i - 1]:
                    i += 1
                backtrack(chosen, remaining[i:], diff)

        backtrack([], candidates, target)
        return res