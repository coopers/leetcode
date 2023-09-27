from collections import deque
from typing import List


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