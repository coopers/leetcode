class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                ch = word[i]
                if ch == ".":
                    return any(dfs(i + 1, n) for n in node.children.values())
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.isWord

        return dfs(0, self.root)