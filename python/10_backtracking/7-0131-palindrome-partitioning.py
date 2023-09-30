from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(s: str, palindromes: List[str]):
            if not s:
                res.append(palindromes)
            else:
                for i in range(1, len(s) + 1):
                    if s[:i] == s[:i][::-1]:
                        dfs(s[i:], palindromes + [s[:i]])
        dfs(s, [])
        return res
    

class Solution:
    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        self.dfs(s, [])
        return self.res

    def dfs(self, s: str, palindromes: List[str]):
        if not s:
            self.res.append(palindromes)
        else:
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    self.dfs(s[i:], palindromes + [s[:i]])