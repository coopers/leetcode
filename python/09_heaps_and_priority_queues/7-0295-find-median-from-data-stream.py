import heapq

# Space: O(N)
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    # Time: O(log(N))
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    # Time: O(1)
    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


class MedianFinder:
    def __init__(self):
        self.lil, self.big = [], []  # maxHeap, minHeap

    def addNum(self, num: int) -> None:
        if self.lil and num < self.lil[0]:
            self.lil.append(num)
            heapq._siftdown_max(self.lil, 0, len(self.lil) - 1)
        else:
            heapq.heappush(self.big, num)

        if len(self.lil) > len(self.big) + 1:
            heapq.heappush(self.big, heapq._heappop_max(self.lil))
        elif len(self.big) > len(self.lil) + 1:
            self.lil.append(heapq.heappop(self.big))
            heapq._siftdown_max(self.lil, 0, len(self.lil) - 1)

    def findMedian(self) -> float:
        if len(self.lil) > len(self.big):
            return self.lil[0]
        elif len(self.big) > len(self.lil):
            return self.big[0]
        return (self.lil[0] + self.big[0]) / 2.0