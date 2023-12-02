from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        hasZeroCol = any(not matrix[r][0] for r in range(ROWS))
        hasZeroRow = any(not matrix[0][c] for c in range(COLS))
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if not matrix[r][c]:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, ROWS):
            if not matrix[r][0]:
                for c in range(1, COLS):
                    matrix[r][c] = 0

        for c in range(1, COLS):
            if not matrix[0][c]:
                for r in range(1, ROWS):
                    matrix[r][c] = 0
        
        if hasZeroCol:
            for r in range(ROWS):
                matrix[r][0] = 0

        if hasZeroRow:
            for c in range(COLS):
                matrix[0][c] = 0