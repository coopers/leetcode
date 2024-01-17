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
            
            index = ord(big[len(lil) + i]) - LOWER_A
            counter[index] += 1
            if counter[index] == 0:
                matches += 1
            elif counter[index] == 1:
                matches -= 1

            index = ord(big[i]) - LOWER_A
            counter[index] -= 1
            if counter[index] == 0:
                matches += 1
            elif counter[index] == -1:
                matches -= 1

        return matches == 26


    

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        LOWER_A = 97            
        counter = [0] * 26
        def index(ch):
            return ord(ch) - LOWER_A

        for ch in s1:
            counter[index(ch)] += 1
        for ch in s2[:len(s1)]:
            counter[index(ch)] -= 1
        if all(c == 0 for c in counter):
            return True

        for i in range(len(s2) - len(s1)):
            j = i + len(s1)
            a, b = index(s2[i]), index(s2[j])
            counter[a] += 1
            counter[b] -= 1
            if not counter[a] and not counter[b] and all(c == 0 for c in counter):
                return True

        return False
    
