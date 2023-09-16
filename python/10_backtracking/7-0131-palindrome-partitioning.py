class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s: str, palindromes: List[str], res: List[List[str]]):
        if not s:
            res.append(palindromes)
        else:
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    self.dfs(s[i:], palindromes + [s[:i]], res)