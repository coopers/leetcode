# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = groupPrev = ListNode(0, head)
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupPrev.next = kth
            groupNext = kth.next

            # reverse group
            prev, node = groupNext, head
            while node != groupNext:
                nxt = node.next
                node.next = prev
                prev, node = node, nxt

            groupPrev, head = head, groupNext
            
        return dummy.next

    def getKth(self, node, k):
        for _ in range(k):
            if node is None:
                return None
            node = node.next
        return node
