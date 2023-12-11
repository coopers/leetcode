# Let N be the length of the string.
# Let M be the number of characters in the alphabet.
# Time   O(N)
# Space  O(min(N, M))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        m = {}
        l = 0
        for r, ch in enumerate(s):
            if ch in m:
                l = max(l, m[ch])

            longest = max(longest, r - l + 1)
            m[ch] = r + 1

        return longest
