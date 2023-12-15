from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time   O(N)
# Space  O(N) if tree is a linked list
#        O(logN) if the tree is balaned
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res
