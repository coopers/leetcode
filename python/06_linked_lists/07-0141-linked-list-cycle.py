# Definition for singly-linked list.
from typing import Optional



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time   O(N + K) where N is the non-cyclic length and K is the cyclic length.
# Space  O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
