from collections import defaultdict


# Time   O(N) chars in string
# Space  O(M) unique chars in counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        maxCount = 0
        l = 0
        for r, ch in enumerate(s):
            counter[ch] += 1
            if counter[ch] > maxCount:
                maxCount = counter[ch]
            elif maxCount + k < r - l + 1:
                counter[s[l]] -= 1
                l += 1
        
        return len(s) - l