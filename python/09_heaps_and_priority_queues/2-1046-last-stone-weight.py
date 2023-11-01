import heapq
from typing import List

# Time   O(N(log(N)))
# Space  O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            diff = heapq.heappop(stones) - stones[0]
            if diff < stones[0]:
                stones[0] = diff
            elif diff:
                heapq.heapreplace(stones, diff)
            else:
                heapq.heappop(stones)

        return 0 if not stones else -stones[0]
    

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            num = heapq.heappop(stones) - heapq.heappop(stones)
            if num:
                heapq.heappush(stones, num)

        return 0 if not stones else -stones[0]


# There's a private _heapify_max method.
# https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
class Solution(object):
    def lastStoneWeight(self, stones):
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)
        
        stones.append(0)
        return stones[0]
