from collections import Counter


# Time   O(N)
# Space  O(1) since the number of letters is constant, 26.


# Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


# dict.get
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for i in range(len(s)):
            counter[s[i]] = 1 + counter.get(s[i], 0)
            counter[t[i]] = counter.get(t[i], 0) - 1
        
        return all(count == 0 for _, count in counter.items())


# Array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1

        for ch in t:
            i = ord(ch) - ord('a')
            counter[i] -= 1
            if counter[i] < 0:
                return False
        
        return sum(counter) == 0
