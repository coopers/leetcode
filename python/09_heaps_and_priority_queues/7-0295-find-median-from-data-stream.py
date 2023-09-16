class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Two heaps of equal size
        self.lil, self.big = [], []  # maxHeap, minHeap

    def addNum(self, num: int) -> None:
        if self.lil and num < -self.lil[0]:
            heapq.heappush(self.lil, -num)
        else:
            heapq.heappush(self.big, num)

        if len(self.lil) > len(self.big) + 1:
            heapq.heappush(self.big, -heapq.heappop(self.lil))
        elif len(self.big) > len(self.lil) + 1:
            heapq.heappush(self.lil, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.lil) > len(self.big):
            return -self.lil[0]
        elif len(self.big) > len(self.lil):
            return self.big[0]
        return (-self.lil[0] + self.big[0]) / 2.0