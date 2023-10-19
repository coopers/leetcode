# Time   O(N)
# Space  O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if l <= r and s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            if l <= r and s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def isAlphaNumeric(self, ch: str) -> bool:
        return (
            'a' <= ch <= 'z' or 
            'A' <= ch <= 'Z' or 
            '0' <= ch <= '9'
        )