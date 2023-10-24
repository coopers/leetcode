from typing import List



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time   O(N)
# Space  O(1)
class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
