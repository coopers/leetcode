# Time   O(N)
# Space  O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for bracket in s:
            if bracket in closeToOpen:
                if not stack or closeToOpen[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)
        
        return not stack