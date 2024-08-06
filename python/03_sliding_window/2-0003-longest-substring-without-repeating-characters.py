# Let N be the length of the string.
# Let M be the number of characters in the alphabet.
# Time   O(N)
# Space  O(min(N, M))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charToIndex = {}
        l = 0
        for r, ch in enumerate(s):
            if ch in charToIndex:
                l = max(l, charToIndex[ch] + 1)
            
            charToIndex[ch] = r
            res = max(res, r - l + 1)
        
        return res
