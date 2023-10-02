from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def patterns(word):
            return [word[:i] + "*" + word[i + 1:] for i in range(len(word))]

        patternToNeighbors = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pattern in patterns(word):
                patternToNeighbors[pattern].append(word)

        visit = set()
        q = deque([beginWord])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for pattern in patterns(word):
                    for neighbor in patternToNeighbors[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
        return 0