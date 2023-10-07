from typing import List


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