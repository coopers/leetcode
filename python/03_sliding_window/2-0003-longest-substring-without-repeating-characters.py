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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        charSet = set()
        for r, ch in enumerate(s):
            while ch in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(ch)
            longest = max(longest, r - l + 1)
        return longest


# Time   O(N)
# Space  O(M)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        longest = 0
        l = 0
        for r, ch in enumerate(s):
            i = chars[ord(ch)]
            if i is not None and i > l:
                l = i + 1

            longest = max(longest, r - l + 1)
            chars[ord(ch)] = r
        return longest