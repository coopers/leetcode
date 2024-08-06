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


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))