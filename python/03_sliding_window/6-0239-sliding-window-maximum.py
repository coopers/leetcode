from collections import deque
from typing import List


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
# Time   O(N)
# Space  O(K)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
                
            q.append(i)

        res.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q[0] == i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)
            res.append(nums[q[0]])

        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for r, n in enumerate(nums):
            while q and n > nums[q[-1]]:
                q.pop()
            q.append(r)
            if r + 1 >= k:
                if q[0] <= r - k:
                    q.popleft()
                res.append(nums[q[0]])
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = 0
        for r, n in enumerate(nums):
            while q and n > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

        return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))