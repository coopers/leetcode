from typing import List




# Time   O(N^2)
# Space  O(N)

class Solution:
    def __init__(self):
        self.res = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i, n in enumerate(nums[:-2]):
            if n > 0:
                break
            if i == 0 or n != nums[i - 1]:
                self.helper(nums[i+1:], -n)
            
        return self.res

    def helper(self, arr: List[int], target):
        l, r = 0, len(arr) - 1
        while l < r:
            total = arr[l] + arr[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                self.res.append([-target, arr[l], arr[r]])
                l += 1
                r -= 1
                while l < r and arr[l] == arr[l - 1]:
                    l += 1
                while l < r and arr[r] == arr[r + 1]:
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
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        nums.sort()
        l = 0
        while l < N - 2 and nums[l] < 1:
            target = -nums[l]
            m = l + 1
            r = N - 1
            while m < r:
                total = nums[m] + nums[r]
                if total < target:
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1

                elif total > target:
                    r -= 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1

                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
            
            l += 1
            while l < N - 2 and nums[l] == nums[l - 1]:
                l += 1
        
        return res     

