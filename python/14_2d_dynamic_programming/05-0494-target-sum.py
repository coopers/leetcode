from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total:
            return 0
        
        dp = [0] * (2 * total + 1)
        dp[total + nums[0]] += 1
        dp[total - nums[0]] += 1
        for n in nums[1:]:
            current = [0] * (2 * total + 1)
            for i, t in enumerate(dp):
                if t:
                    current[i + n] += t
                    current[i - n] += t
        
            dp = current
        
        return dp[target + total]