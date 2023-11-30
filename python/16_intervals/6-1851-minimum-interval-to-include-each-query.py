import heapq


L = SIZE = 0
R = 1
class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort(reverse=True)
        h = []
        res = {}
        for m in sorted(queries):
            while intervals and intervals[-1][L] <= m:
                l, r = intervals.pop()
                if m <= r:
                    heapq.heappush(h, [r - l + 1, r])

            while h and h[0][R] < m:
                heapq.heappop(h)
            
            res[m] = h[0][SIZE] if h else -1

        return [res[q] for q in queries]