class Trie:
    def __init__(self):
        self.root = {}
        self.words = set()

    # Time   O(N) where N is the number of nodes in the word.
    # Space  O(N)
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        self.words.add(id(node))

    # Time   O(N) where N is the number of nodes in the word.
    # Space  O(1)
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return id(node) in self.words

    # Time   O(N) where N is the number of nodes in the word.
    # Space  O(1)
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True



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
        