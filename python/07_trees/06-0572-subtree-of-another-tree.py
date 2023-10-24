# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time   O(MN), which can be reduced to O(M+N) using other approaches
# Space  O(M+N)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p == q
            
        return p.val == q.val and \
               self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root == subRoot
            
        return self.isSameTree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)
