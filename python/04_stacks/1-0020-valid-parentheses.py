# Time   O(N)
# Space  O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        closingToOpening = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for bracket in s:
            if bracket in closingToOpening:
                if not stack or closingToOpening[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)
        
        return not stack