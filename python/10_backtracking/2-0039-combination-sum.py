from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(chosen, remaining, total):
            if total == target:
                res.append(chosen)
            elif remaining and total < target:
                helper(chosen + [remaining[0]], remaining, total + remaining[0])
                helper(chosen, remaining[1:], total)

        helper([], candidates, 0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        chosen = []

        def dfs(i, total):
            if total == target:
                res.append(chosen.copy())
            elif i < len(candidates) and total < target:
                chosen.append(candidates[i])
                dfs(i, total + candidates[i])
                chosen.pop()
                dfs(i + 1, total)

        dfs(0, 0)
        return res