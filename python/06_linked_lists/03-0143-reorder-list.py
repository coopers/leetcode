class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        node = slow.next
        prev = slow.next = None
        while node:
            nxt = node.next
            node.next = prev
            prev, node = node, nxt

        # merge two halfs
        a, b = head, prev
        while b:
            aNext, bNext = a.next, b.next
            a.next = b
            b.next = aNext
            a, b = aNext, bNext