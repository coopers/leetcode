from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target):
            return 0
        
        prev = defaultdict(int)
        prev[total + nums[0]] += 1
        prev[total - nums[0]] += 1
        for n in nums[1:]:
            curr = defaultdict(int)
            for k, v in prev.items():
                curr[k + n] += v
                curr[k - n] += v
                
            prev = curr

        return prev[target + total]
    
    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total:
            return 0
        
        prev = [0] * (2 * total + 1)
        prev[total + nums[0]] += 1
        prev[total - nums[0]] += 1
        for n in nums[1:]:
            current = [0] * (2 * total + 1)
            for i, t in enumerate(prev):
                if t:
                    current[i + n] += t
                    current[i - n] += t
        
            prev = current
        
        return prev[target + total]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total:
            return 0
        
        cur = [0] * (2 * total + 1)
        nxt = cur[:]
        cur[total + nums[0]] += 1
        cur[total - nums[0]] += 1
        for n in nums[1:]:
            for i, t in enumerate(cur):
                if t:
                    nxt[i + n] += t
                    nxt[i - n] += t
                    cur[i] = 0
        
            cur, nxt = nxt, cur
        
        return cur[target + total]
    
nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target))

