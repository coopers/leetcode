from typing import List
from collections import Counter
import heapq



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # O(N) time
        counter = Counter(nums)   

        # O(N log k) time
        return heapq.nlargest(k, counter.keys(), key=counter.get)
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h = [(-count, num) for num, count in counter.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h = [(-count, num) for num, count in counter.items()]

        heapq.heapify(h)
        res = []
        for _ in range(k):
            _, num = heapq.heappop(h)
            res.append(num)
        return res
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            freq[count].append(num)

        res = []
        for values in reversed(freq):
            for value in values:
                res.append(value)
                if len(res) == k:
                    return res
