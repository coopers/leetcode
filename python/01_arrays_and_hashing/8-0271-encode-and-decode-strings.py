from typing import List


# Let N be the number of characters.
# Let K be the number of strings.
# Time   O(N)
# Space  O(K)

class Codec:
    def encode(self, strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        strs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strs.append(s[i:j])
            i = j
            
        return strs


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            res.append(s[i:j])
            i = j
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))