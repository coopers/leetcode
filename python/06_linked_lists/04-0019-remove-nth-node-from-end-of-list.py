from typing import Optional



# Time   O(N) where N is length of linked list
# Space  O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        node = head
        for _ in range(n):
            node = node.next

        while node:
            prev, node = prev.next, node.next

        prev.next = prev.next.next
        return dummy.next
