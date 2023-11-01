import math



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Time   O(N) where N is the number of nodes in the tree.
# Space  O(N)
class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, -math.inf)
        return self.count
    
    def dfs(self, root: TreeNode, maxVal) -> None:
        if not root:
            return
        
        if root.val >= maxVal:
            maxVal = root.val
            self.count += 1

        self.dfs(root.left, maxVal)
        self.dfs(root.right, maxVal)



class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            nonlocal count
            if node.val >= maxVal:
                maxVal = node.val
                count += 1
            if node.right:
                dfs(node.right, maxVal)
            if node.left:
                dfs(node.left, maxVal)
        
        count = 0
        dfs(root, root.val)
        return count
