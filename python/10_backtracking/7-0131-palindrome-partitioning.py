from collections import defaultdict
from typing import List


# N: the length of the string
# Time:  O(N ✖️ 2^N), worst case all possible substrings are palindromes
# Space: O(N), space used to store the recursion stack, with max depth N.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(chosen: List[str], remaining: str):
            if not remaining:
                res.append(chosen)
            else:
                for i in range(1, len(remaining) + 1):
                    if remaining[:i] == remaining[:i][::-1]:
                        helper(chosen + [remaining[:i]], remaining[i:])
        helper([], s)
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


class Solution:
    def __init__(self):
        self.res = []
        self.palindromeIndices = defaultdict(list)

    def indexAllPalindromes(self, s: str):        
        oneChars = {(i, i + 1) for i in range(len(s))}
        twoChars = {(i - 1, i + 1) for i in range(1, len(s)) if s[i - 1] == s[i]}
        current = oneChars | twoChars
        while current:
            nxt = set()
            for i, j in current:
                self.palindromeIndices[i].append(j)
                if i > 0 and j < len(s) and s[i-1] == s[j]:
                    nxt.add((i-1, j+1))
            current = nxt

    def permute(self, s: str):
        def helper(palindromes, i):
            if i == len(s):
                self.res.append(palindromes)
            else:
                for j in self.palindromeIndices[i]:
                    helper(palindromes + [s[i:j]], j)

        helper([], 0)

    def partition(self, s: str) -> List[List[str]]:
        self.indexAllPalindromes(s)
        self.permute(s)
        return self.res