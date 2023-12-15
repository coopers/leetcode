class Trie:
    WORD_KEY = '#'
    
    def __init__(self):
        self.root = {}

    # Time   O(N) where N is the number of nodes in the word.
    # Space  O(N)
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[Trie.WORD_KEY] = None

    # Time   O(N) where N is the number of nodes in the word.
    # Space  O(1)
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return Trie.WORD_KEY in node

    # Time   O(N) where N is the number of nodes in the word.
    # Space  O(1)
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

