# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = node = ListNode()

        num = 0
        while l1 or l2 or num:
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next

            node.next = ListNode(num % 10)
            node = node.next
            num //= 10

        return dummy.next
