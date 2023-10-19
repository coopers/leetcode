from typing import List




# Time   O(N^2)
# Space  O(N)

class Solution:
    def __init__(self):
        self.res = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSumII(nums, i)
        return self.res

    def twoSumII(self, nums: List[int], i: int):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                self.res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while hi > lo and nums[hi] == nums[hi + 1]:
                    hi -= 1




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0
        while l < len(nums) - 2 and nums[l] <= 0:
            m = l + 1
            r = len(nums) - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total < 0:
                    m += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    temp = nums[m]
                    while m < r and nums[m] == temp:
                        m += 1
                    temp = nums[r]
                    while r > m and nums[r] == temp:
                        r -= 1
            temp = nums[l]
            while l < len(nums) - 2 and nums[l] == temp:
                l += 1
        return res