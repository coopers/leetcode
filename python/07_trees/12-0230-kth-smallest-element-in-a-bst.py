# Definition for a binary tree node.
from typing import Optional



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time   O(H + k) where H is the height of the tree
#        O(logN + k) when tree is balanced
#        O(N + k) when tree is completely unbalanced,
#        a linked list on the left subtree.

# Space  O(H)
#        O(logN) when the tree is balance
#        O(N) in the worst case
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right
