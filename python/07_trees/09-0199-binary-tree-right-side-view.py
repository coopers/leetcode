from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time   O(N)
# Space  O(D) where D is the diameter of the tree.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        while q:
            res.append(q[0].val)
            for _ in range(len(q)):
                n = q.popleft()
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
        return res
