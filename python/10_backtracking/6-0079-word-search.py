from typing import List


# N: number of cells in the board
# L: length of the word
# Time:  O(N ✖️ 3^L)
# Space: O(L)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        MOVES = ((1,0),(-1,0),(0,1),(0,-1))

        first = last = 0
        for r in range(ROWS):
            for c in range(COLS):
                if word[0] == board[r][c]:
                    first += 1
                elif word[-1] == board[r][c]:
                    last += 1
                    
        if last < first:
            word = word[::-1]

        def helper(r, c, i):
            if i == len(word):
                return True

            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == word[i]
            ):
                board[r][c] = ''
                i += 1
                for dr, dc in MOVES:
                    row, col = r + dr, c + dc
                    if helper(row, col, i):
                        return True
                        
                board[r][c] = word[i-1]

        return any(helper(r, c, 0) for r in range(ROWS) for c in range(COLS))