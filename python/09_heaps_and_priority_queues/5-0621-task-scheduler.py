import heapq
from typing import List
from collections import Counter, deque

# Greedy
# Time   O(N), where N is the number of tasks
# Space  O(1), since the tasks are lettes 'A'-'Z'
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maximum = max(counter.values())
        num_maxes = sum(v == maximum for v in counter.values())
        min_time = (maximum - 1) * (n + 1) + num_maxes
        return max(min_time, len(tasks))
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
