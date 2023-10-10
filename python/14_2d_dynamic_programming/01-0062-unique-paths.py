class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lil, big = m, n
        if n < m:
            lil, big = n, m
        row = [1] * lil
        for _ in range(big - 1):
            new_row = row[:]
            for i in range(1, lil):
                new_row[i] += new_row[i - 1]
            row = new_row
        return row[lil - 1]