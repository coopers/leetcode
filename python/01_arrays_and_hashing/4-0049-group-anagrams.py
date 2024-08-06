from typing import List
from collections import defaultdict


# Time   O(NK) where N is len(strs) and K is max len(s) for s in strs
# We examine each string and each character in linear time.
# Space  O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToAnagrams = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for ch in s:
                counter[ord(ch) - ord('a')] += 1

            keyToAnagrams[tuple(counter)].append(s)
        
        return keyToAnagrams.values()

# Decomposed this using a getAnagramKey function.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToAnagrams = defaultdict(list)
        for s in strs:
            keyToAnagrams[self.getAnagramKey(s)].append(s)
            
        return keyToAnagrams.values()
    
    def getAnagramKey(self, s: str) -> tuple:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        
        return tuple(counts)

# Use setdefault when not using defaultdict
        # d = {}
        # for s in strs:
        #     k = getAnagramKey(s)
        #     d.setdefault(k, []).append(s)
            
        # return d.values()