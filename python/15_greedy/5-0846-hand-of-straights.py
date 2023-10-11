import heapq
from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counter = Counter(hand)
        h = list(counter.keys())
        heapq.heapify(h)
        while h:
            n = heapq.heappop(h)
            while counter[n]:
                counter[n] -= 1
                for i in range(n + 1, n + groupSize):
                    if i not in counter or not counter[i]:
                        return False
                    counter[i] -= 1
        
        return True
