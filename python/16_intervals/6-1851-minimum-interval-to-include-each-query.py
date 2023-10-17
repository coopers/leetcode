import heapq


START = SIZE = 0
END = 1
class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort(reverse=True)
        h = []
        res = {}
        for q in sorted(queries):
            while intervals and intervals[-1][START] <= q:
                l, r = intervals.pop()
                if r >= q:
                    heapq.heappush(h, [r - l + 1, r])

            while h and h[0][END] < q:
                heapq.heappop(h)
            
            res[q] = h[0][SIZE] if h else -1

        return [res[q] for q in queries]