from typing import List
from collections import Counter


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
