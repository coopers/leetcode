class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(chosen, remaining):
            if not remaining:
                res.append(chosen)
            else:
                for i in range(len(remaining)):
                    nextChosen = chosen + [remaining[i]]
                    nextRemaining = remaining[:i] + remaining[i + 1:]
                    helper(nextChosen, nextRemaining)

        helper([], nums)
        return res