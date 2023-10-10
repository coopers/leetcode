class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        # If s1 doesn't reference the shortest string, swap them.
        if len(s2) < len(s1):
            s1, s2 = s2, s1
        
        
        # The previous and current column starts with all 0's and like 
        # before is 1 more than the length of the first word.
        previous = [0] * (len(s1) + 1)
        current  = [0] * (len(s1) + 1)
        
        # Iterate up each column, starting from the last one.
        for j in reversed(range(len(s2))):
            for i in reversed(range(len(s1))):
                if s1[i] == s2[j]:
                    current[i] = 1 + previous[i + 1]
                else:
                    current[i] = max(previous[i], current[i + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]