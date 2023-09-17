class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if n in m:
                return [i, m[n]]
            m[target - n] = i
