class WordDictionary:
    WORD_KEY = '#'
    def __init__(self):
        self.root = {}

# Time:  O(M) where M is the length of the word.
# Space: O(M)
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[WordDictionary.WORD_KEY] = None

# Time:  O(M) where M is the length of a defined word, has no '.' characters
#        O(N✖️26^M) for undefined words (with '.' characters)
# Space: O(1) for well-defined words
#        O(M) for undefined words to keep track of recursion.
    def search(self, word: str) -> bool:
        def dfs(word, node):
            if node is None:
                return False
            
            if word == '':
                return WordDictionary.WORD_KEY in node

            ch, word = word[0], word[1:]
            if ch == '.':
                return any(dfs(word, n) for n in node.values())
            elif ch in node:
                return dfs(word, node[ch])
            else:
                return False
        
        return dfs(word, self.root)


class WordDictionary:
    WORD_KEY = '#'
    def __init__(self):
        self.root = {}
        self.words = set()

# Time:  O(M) where M is the length of the word.
# Space: O(M)
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        self.words.add(id(node))

# Time:  O(M) where M is the length of a defined word, has no '.' characters
#        O(N✖️26^M) for undefined words (with '.' characters)
# Space: O(1) for well-defined words
#        O(M) for undefined words to keep track of recursion.
    def search(self, word: str) -> bool:
        def dfs(word, node):
            if word == '':
                return id(node) in self.words

            ch, word = word[0], word[1:]
            if ch == '.':
                return any(dfs(word, n) for n in node.values())
            elif ch in node:
                return dfs(word, node[ch])
            else:
                return False
        
        return dfs(word, self.root)

