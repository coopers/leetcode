from typing import Optional




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
# Time   O(N + M) where N and M are the lengths of the linked lists.
# Space  O(1)
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        while a and b:
            if a.val < b.val:
                head.next = a
                a = a.next
            else:
                head.next = b
                b = b.next

            head = head.next
        
        head.next = a or b
        return dummy.next


# Recursive
# Time   O(N + M) where N and M are the lengths of the linked lists.
# Space  O(N + M) where N and M are the lengths of the linked lists.
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a or not b:
            return a or b
        lil, big = (a, b) if a.val < b.val else (b, a)
        lil.next = self.mergeTwoLists(lil.next, big)
        return lil
