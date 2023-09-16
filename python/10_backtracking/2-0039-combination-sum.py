class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(chosen, remaining, diff):
            if not diff:
                res.append(chosen)
            if diff > 0 and remaining:
                helper(chosen + [remaining[0]], remaining, diff - remaining[0])
                helper(chosen, remaining[1:], diff)

        helper([], candidates, target)
        return res
