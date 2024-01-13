from typing import List


# Let N be the number of characters.
# Let K be the number of strings.
# Time   O(N)
# Space  O(K)

class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0
        while l < len(s):
            while s[r] != '#':
                r += 1
            strlen = int(s[l:r])
            l = r + 1
            r = l + strlen
            res.append(s[l:r])
            l = r

        return res


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