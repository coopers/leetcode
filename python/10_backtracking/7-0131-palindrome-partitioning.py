class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s: str, path: List[str], res: List[List[str]]):
        if not s:
            res.append(path)
        else:
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    self.dfs(s[i:], path + [s[:i]], res)