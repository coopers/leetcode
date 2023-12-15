from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time   O(N) where N is length of linked list
# Space  O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt, head.next = head.next, prev
            prev, head = head, nxt
            
        return prev
