from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for L in range(N-2, 0, -1):
            for R in range(L, N-1):
                p = nums[L-1] * nums[R+1]
                dp[L][R] = max(p * nums[i] + dp[L][i-1] + dp[i+1][R] for i in range(L, R+1))
        return dp[1][-2]

assert Solution().maxCoins([3,1,5,8]) == 167

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1] + nums + [1]
#         dp = {}

#         def dfs(l, r):
#             if l > r:
#                 return 0
#             if (l, r) in dp:
#                 return dp[(l, r)]
            
#             dp[(l, r)] = 0
#             for i in range(l, r + 1):
#                 coins = nums[l - 1] * nums[i] * nums[r + 1]
#                 coins += dfs(l, i - 1) + dfs(i + 1, r)
#                 dp[(l, r)] = max(dp[(l, r)], coins)
#             return dp[(l, r)]
#         return dfs(1, len(nums) - 2)

