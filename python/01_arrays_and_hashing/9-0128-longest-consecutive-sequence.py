class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for n in s:
            if n - 1 in s:
                continue
            num = n
            while num in s:
                num += 1
            res = max(res, num - n)
        return res