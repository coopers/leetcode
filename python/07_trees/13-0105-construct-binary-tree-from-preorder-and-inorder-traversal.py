from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            i = inorder.index(preorder.pop(0))
            return TreeNode(
                val=inorder[i],
                left=self.buildTree(preorder, inorder[:i]),
                right=self.buildTree(preorder, inorder[i + 1:])
            )
