class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left, right = dummy, head

        for _ in range(n):
            right = right.next

        while right:
            left, right = left.next, right.next

        # delete
        left.next = left.next.next
        return dummy.next
