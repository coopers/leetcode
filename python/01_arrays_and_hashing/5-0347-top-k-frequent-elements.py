from typing import List
from collections import Counter
import heapq


# O(N) time
# O(N) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequencyToNums = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            frequencyToNums[count].append(num)

        res = []
        for nums in reversed(frequencyToNums):
            for num in nums:
                res.append(num)
                if len(res) == k:
                    return res

# We can use a dictionary instead of a nested list,
# but it is not as efficient.
#
# We have to sort the keys in the dictionary. 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequencyToNums = {}
        for num, count in counter.items():
            frequencyToNums.setdefault(count, []).append(num)

        res = []
        for count in sorted(frequencyToNums.keys(), reverse=True):
            for num in frequencyToNums[count]:
                res.append(num)
                if len(res) == k:
                    return res
                

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # O(N) time
        counter = Counter(nums)   

        # O(N log k) time
        return heapq.nlargest(k, counter, key=counter.get)
