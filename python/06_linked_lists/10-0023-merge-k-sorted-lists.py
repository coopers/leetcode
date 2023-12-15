from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time   O(N log K) where K is the number of linked lists
# Space  O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(a, b))
            lists = mergedLists
        return lists[0] if lists else None

    def mergeList(self, a, b):
        dummy = node = ListNode()
        while a and b:
            if a.val < b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next

        node.next = a or b
        return dummy.next
