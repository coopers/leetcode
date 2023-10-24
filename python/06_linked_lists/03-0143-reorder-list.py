from typing import Optional



# Time   O(N) where N is length of linked list
# Space  O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        second = self.reverseList(second)

        dummy = head
        while head:
            nxt = head.next 
            head.next = second
            head = head.next
            second = nxt
        return dummy

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev, head = head, nxt
        return prev