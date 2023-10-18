from typing import List
from collections import defaultdict


# N = Board length
# Time   O(N^2)
# Space  O(N^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(N):
            for c in range(N):
                if board[r][c] != '.':
                    val = board[r][c]
                    b = r // 3 * 3 + c // 3 
                    if (
                        val in row[r] or
                        val in col[c] or
                        val in box[b]
                    ):
                        return False
                        
                    row[r].add(val)
                    col[c].add(val)
                    box[b].add(val)

        return True
    

# Use N-sized binary digits to store data
# N = Board length
# Time   O(N^2)
# Space  O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row = [0] * N
        col = [0] * N
        box = [0] * N
        for r in range(N):
            for c in range(N):
                if board[r][c] != '.':
                    i = 1 << (int(board[r][c]) - 1)
                    b = r // 3 * 3 + c // 3 
                    if (
                        row[r] & i or
                        col[c] & i or
                        box[b] & i
                    ):
                        return False
                        
                    row[r] |= i
                    col[c] |= i
                    box[b] |= i

        return True