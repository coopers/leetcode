# Time   O(L1 + (L2 - L1))
# Space  O(1)

class Solution:
    def checkInclusion(self, lil: str, big: str) -> bool:
        if len(lil) > len(big):
            return False

        LOWER_A = 97
        counter = [0] * 26
        for ch in lil:
            counter[ord(ch) - LOWER_A] -= 1
        
        for ch in big[:len(lil)]:
            counter[ord(ch) - LOWER_A] += 1
        
        matches = sum(n == 0 for n in counter)

        for i in range(len(big) - len(lil)):
            if matches == 26:
                return True

            index = ord(big[i]) - LOWER_A
            counter[index] -= 1
            if counter[index] == 0:
                matches += 1
            elif counter[index] == -1:
                matches -= 1

            index = ord(big[i + len(lil)]) - LOWER_A
            counter[index] += 1
            if counter[index] == 0:
                matches += 1
            elif counter[index] == 1:
                matches -= 1

        return matches == 26


# Less optimized solution where we count the 26 possible matches
# in each iteration of the window.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counter = [0] * 26
        for ch in s1:
            counter[ord(ch) - ord('a')] += 1
        
        for i in range(len(s1)):
            counter[ord(s2[i]) - ord('a')] -= 1
        
        for i in range(len(s2) - len(s1)):
            if all(count == 0 for count in counter):
                return True
            
            j = i + len(s1)
            counter[ord(s2[i]) - ord('a')] += 1
            counter[ord(s2[j]) - ord('a')] -= 1
        
        return all(count == 0 for count in counter)
    
