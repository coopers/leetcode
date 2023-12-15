from typing import Optional



# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# Time   O(N) where N is length of linked list
# Space  O(N)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {None: None}
        n = head
        while n:
            m[n] = Node(n.val)
            n = n.next
        
        n = head
        while n:
            copy = m[n]
            copy.next = m[n.next]
            copy.random = m[n.random]
            n = n.next

        return m[head]


# Time   O(N) where N is length of linked list
# Space  O(1)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        n = head
        while n:
            node = Node(n.val, n.next)
            n.next = node
            n = n.next.next
        
        n = head
        while n:
            n.next.random = n.random.next if n.random else None
            n = n.next.next
        
        headCopy = head.next
        n = head
        while n.next.next:
            nxt = n.next.next
            node = n.next
            node.next = node.next.next
            n = nxt

        return headCopy