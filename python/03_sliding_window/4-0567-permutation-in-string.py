# Time   O(L1 + (L2 - L1))
# Space  O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        counter = [0] * 26
        for ch in s1:
            i = ord(ch) - ord('a')
            counter[i] -= 1

        for ch in s2[:l1]:
            i = ord(ch) - ord('a')
            counter[i] += 1
        
        matches = 0
        for c in counter:
            if c == 0:
                matches += 1

        for r in range(l1, l2):
            if matches == 26:
                return True
            
            i = ord(s2[r - l1]) - ord('a')
            if counter[i] == 0:
                matches -= 1
            elif counter[i] == 1:
                matches += 1
            counter[i] -= 1

            i = ord(s2[r]) - ord('a')
            if counter[i] == -1:
                matches += 1
            elif counter[i] == 0:
                matches -= 1
            counter[i] += 1

        return matches == 26