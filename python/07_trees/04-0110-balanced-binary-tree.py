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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]
    
    def helper(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return (True, 0)
        
        lBal, lDepth = self.helper(root.left)
        if not lBal:
            return (False, 0)
        
        rBal, rDepth = self.helper(root.right)
        if not rBal:
            return (False, 0)
        
        return (abs(lDepth - rDepth) <= 1, 1 + max(lDepth, rDepth))
