from typing import List


# Union-Find
# Time:  O(V + E ✖️ ⍺(V)) where V is the number of nodes
# Space: O(V)
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while n != self.parent[n]:
            n, self.parent[n] = self.parent[n], self.parent[self.parent[n]]
        return n

    def union(self, a, b):
        child, parent = self.find(a), self.find(b)
        if child == parent:
            return False
        
        if self.rank[parent] < self.rank[child]:
            child, parent = parent, child
        
        self.parent[child] = parent
        self.rank[parent] += self.rank[child]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionfind = UnionFind(n)
        count = n
        for i, j in edges:
            if unionfind.union(i, j):
                count -= 1

        return count


# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        visit = [False] * n
        def dfs(i):
            if visit[i]:
                return 0

            visit[i] = True
            for j in neighbors[i]:
                dfs(j)
            return 1

        return sum(dfs(i) for i in range(n))


