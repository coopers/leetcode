# Time   O(N)
# Space  O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for ch in s:
            if ch in brackets:
                if not stack or brackets[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        
        return not stack