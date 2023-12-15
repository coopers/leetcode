from typing import List



# Time:  O(M(4✖️3^(L - 1)))
# M is the number of squares on the board
# L is the length of the longest word
# There are 4 possible directions,
# but 3 options remain,
# since we cannot revisit where we have been.

# Space: O(N) where N is the total number of
# characters in all words, when they do not overlap.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        WORD_KEY = '#'
        matchedWords = []
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        def backtrack(row, col, parent):
            letter = board[row][col]
            node = parent[letter]
            word_match = node.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)

            board[row][col] = ''
            for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r, c = row + dr, col + dc
                if (
                    0 <= r < ROWS and
                    0 <= c < COLS and
                    board[r][c] in node
                ):
                    backtrack(r, c, node)

            board[row][col] = letter
            if not node:
                parent.pop(letter)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in trie:
                    backtrack(row, col, trie)

        return matchedWords
    