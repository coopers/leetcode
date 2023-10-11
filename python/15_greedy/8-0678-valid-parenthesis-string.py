# Greedy: O(n)
class Solution:
    def checkValidString(self, s):
        left_min = left_max = 0
        for c in s:
            if c == '(':
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ')':
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            
            if left_max < 0:
                return False
            
            if left_min < 0:
                left_min = 0
            
        return left_min == 0
    

# Dynamic Programming: O(n^2)
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}  # key=(i, leftCount) -> isValid

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]

            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (
                    dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left)
                )
            return dp[(i, left)]

        return dfs(0, 0)
