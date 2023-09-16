class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index, n):
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    return any(dfs(i + 1, child) for child in n.children.values())
                else:
                    if c not in n.children:
                        return False
                    n = n.children[c]
            return n.isWord

        return dfs(0, self.root)