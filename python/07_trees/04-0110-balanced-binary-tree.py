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
        def dfs(n):
            if not n:
                return (True, 0)
            
            balanced, left = dfs(n.left)
            if not balanced:
                return (False, 0)

            balanced, right = dfs(n.right)
            if not balanced:
                return (False, 0)

            if abs(left - right) > 1:
                return (False, 0)
            
            return (True, max(left, right) + 1)

        return dfs(root)[0]
