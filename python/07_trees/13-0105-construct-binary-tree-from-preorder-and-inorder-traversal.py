from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time   O(N)
# Space  O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        m = {n: i for i, n in enumerate(inorder)}
        p = 0
        def helper(l, r):
            if l > r:
                return None

            nonlocal p
            value = preorder[p]
            p += 1
            root = TreeNode(value)
            i = m[value]
            root.left = helper(l, i - 1)
            root.right = helper(i + 1, r)
            return root

        return helper(0, len(preorder) - 1)
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            i = inorder.index(preorder.pop(0))
            return TreeNode(
                val=inorder[i],
                left=self.buildTree(preorder, inorder[:i]),
                right=self.buildTree(preorder, inorder[i + 1:])
            )
        
