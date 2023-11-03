from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


# Time:  O(N + M), where N is the number of nodes and M is the number of edges
# Space: O(N), the space of visited and the depth of the recursion stack
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone = Node(node.val)
        self.visited[node] = clone
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone