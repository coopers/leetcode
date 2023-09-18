from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        def isValidCell(r, c):
            if board[r][c] == ".":
                return True
            
            n = board[r][c]
            b = (r // 3, c // 3)
            if (
                n in row[r]
                or n in col[c]
                or n in box[b]
            ):
                return False
            
            row[r].add(n)
            col[c].add(n)
            box[b].add(n)
            return True
        
        return all(isValidCell(r, c) for r in range(9) for c in range(9))
                                                                               