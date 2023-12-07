from typing import List



# Time   O(N)
# Space  O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for lil in s:
            if lil - 1 not in s:
                big = lil + 1
                while big in s:
                    big += 1
         
                longest = max(longest, big - lil)
        
        return longest