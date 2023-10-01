class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        
        nodeToClone = {}
        def dfs(node):
            if node in nodeToClone:
                return nodeToClone[node]

            clone = Node(node.val)
            nodeToClone[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)