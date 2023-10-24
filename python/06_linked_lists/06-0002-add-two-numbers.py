from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time   O(max(M, N)) where M and N are the lengths of the linked lists
# Space  O(1)

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

            num, val = divmod(num, 10)
            node.next = ListNode(val)
            node = node.next

        return dummy.next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = prev = ListNode()

        while l1 and l2:
            total = l1.val + l2.val + carry
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0

            prev.next = ListNode(total)
            l1, l2, prev = l1.next, l2.next, prev.next
        
        l = l1 or l2
        while l:
            total = l.val + carry
            if total > 9:
                carry = 1
                total = 0
            else:
                carry = 0
            
            prev.next = ListNode(total)
            l, prev = l.next, prev.next
        
        if carry:
            prev.next = ListNode(carry)

        return dummy.next