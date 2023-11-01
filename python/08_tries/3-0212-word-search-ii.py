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
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        def backtrack(row, col, parent):
            letter = board[row][col]
            node = parent[letter]
            # check if we find a match of word
            word_match = node.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                # as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = ''

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r, c = row + dr, col + dc
                if (
                    0 <= r < ROWS and
                    0 <= c < COLS and
                    board[r][c] in node
                ):
                    backtrack(r, c, node)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not node:
                parent.pop(letter)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in trie:
                    backtrack(row, col, trie)

        return matchedWords
    



class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        node = self
        node.refs += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.refs += 1
        node.isWord = True

    def removeWord(self, word):
        node = self
        node.refs -= 1
        for ch in word:
            node = node.children[ch]
            node.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        res = []
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] in node.children and
                node.children[board[r][c]].refs
            ):            
                ch = board[r][c]
                word += ch
                node = node.children[ch]
                board[r][c] = ''
                if node.isWord:
                    node.isWord = False
                    res.append(word)
                    root.removeWord(word)

                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)

                board[r][c] = ch

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return res