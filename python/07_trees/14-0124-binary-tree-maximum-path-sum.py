import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf

        def dfs(root):
            if not root:
                return 0
                
            nonlocal res
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            res = max(res, left + right + root.val)
            return max(left, right) + root.val
        
        dfs(root)
        return res
