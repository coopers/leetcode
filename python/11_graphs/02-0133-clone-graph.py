class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        nodeToClone = {}

        def dfs(node):
            if node in nodeToClone:
                return nodeToClone[node]

            clone = Node(node.val)
            nodeToClone[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node) if node else None