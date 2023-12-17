import heapq

# Space: O(N)
class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    # Time: O(log(N))
    def addNum(self, num):
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))
        else:
            heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))

    # Time: O(1)
    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return float(self.minheap[0] - self.maxheap[0]) / 2
        else:
            return float(self.minheap[0])