from typing import List



# Time   O(4^N / SQRT(N))
# Space  O(N)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if closedN == n:
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

print(Solution().generateParenthesis(2))