class WordDictionary:
    def __init__(self):
        self.trie = {}
        self.words = set()

# Time:  O(M) where M is the length of the word.
# Space: O(M)
    def addWord(self, word: str) -> None:
        node = self.trie
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
        def dfs(word, node) -> bool:
            for i, ch in enumerate(word):
                if ch in node:
                    node = node[ch]
                elif ch == '.':
                    return any(dfs(word[i + 1:], n) for n in node.values())
                else:
                    return False

            return id(node) in self.words

        return dfs(word, self.trie)



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