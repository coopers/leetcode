import heapq
from typing import List

# Time:  O(N(logN) + M(logK))
#
#        Init
#        Heapify: O(N)
#        When k is 1, there are N calls of log(N) operations
#        O(N + N(logN))
#
#        Add
#        Each call to add can result in an add and remove from the heap.
#        O(M ✖️ log(k))
#       
# Space: O(N) when we initialize the heap
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
