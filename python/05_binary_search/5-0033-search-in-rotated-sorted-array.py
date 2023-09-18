from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while True:
            if l > r:
                return -1
            
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[mid] > nums[r]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

nums = [3,1]
target = 1
print(Solution().search(nums, target))