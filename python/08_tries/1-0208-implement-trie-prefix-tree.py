class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.word

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        