from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = left + (right - left) // 2
            r, c = divmod(mid, COLS)
            if matrix[r][c] < target:
                left = mid + 1
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                return True

        return False