import math
from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time   O(N)
# Space  O(N)
class Solution:
    def validate(self, node: Optional[TreeNode], lo, hi) -> bool:
        if not node:
            return True
        
        if not (lo < node.val < hi):
            return False

        return self.validate(node.left, lo, node.val) and \
               self.validate(node.right, node.val, hi)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)
    
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBetween(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False

            return (isBetween(node.left, low, node.val) and \
                    isBetween(node.right, node.val, high))

        return isBetween(root, float('-inf'), float('inf'))