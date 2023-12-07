from typing import List




# Time   O(N^2)
# Space  O(N)

class Solution:
    def __init__(self):
        self.res = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.helper(nums, i)
        return self.res

    def helper(self, nums: List[int], i: int):
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                self.res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1




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
                    m += 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
                    r -= 1
                    while r > m and nums[r] == nums[r+1]:
                        r -= 1
            l += 1
            while l < len(nums) - 2 and nums[l] == nums[l-1]:
                l += 1
        return res