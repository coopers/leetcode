from typing import List



# Time   O(N)
# Space  O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i - 1 not in s:
                j = i + 1
                while j in s:
                    j += 1
         
                longest = max(longest, j - i)
        
        return longest