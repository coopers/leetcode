class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * m
        for _ in range(n - 1):
            for i in range(1, m):
                row[i] += row[i - 1]
        
        return row[-1]