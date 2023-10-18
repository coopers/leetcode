from typing import List
from collections import defaultdict



# Time   O(NK) where N is len(strs) and K is max len(s) for S in strs
# We examine each string and each character in linear time.
# Space  O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for ch in s:
                counter[ord(ch) - ord('a')] += 1

            anagrams[tuple(counter)].append(s)
        
        return anagrams.values()
