from collections import defaultdict



# Time   O(N) chars in string
# Space  O(M) unique chars in counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        maxF = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            maxF = max(maxF, counter[s[r]])
            if maxF + k < r - l + 1:
                counter[s[l]] -= 1
                l += 1

        return len(s) - l