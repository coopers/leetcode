from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while True:
            if l > r:
                return False
            
            m = l + (r - l) // 2
            row, col = divmod(m, COLS)
            n = matrix[row][col]
            if n < target:
                l = m + 1
            elif n > target:
                r = m - 1
            else:
                return True