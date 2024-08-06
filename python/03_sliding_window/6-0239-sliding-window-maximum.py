from collections import deque
from typing import List


# Time   O(N)
# Space  O(K)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()

            q.append(i)
            if i >= k - 1:
                if q[0] == i - k:
                    q.popleft()
                    
                res.append(nums[q[0]])
        
        return res
