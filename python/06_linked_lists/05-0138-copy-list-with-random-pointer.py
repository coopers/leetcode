# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        oldToCopy = {None: None}
        node = head
        while node:
            oldToCopy[node] = Node(node.val)
            node = node.next
            
        node = head
        while node:
            copy = oldToCopy[node]
            copy.next = oldToCopy[node.next]
            copy.random = oldToCopy[node.random]
            node = node.next

        return oldToCopy[head]
