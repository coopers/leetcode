from typing import List



# UnionFind
# Time:  O(N ✖️ ⍺(N))
# Space: O(N)
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, n):
        if n != self.parents[n]:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        
        child, parent = (a, b) if self.ranks[a] < self.ranks[b] else (b, a)
        self.parents[child] = parent
        self.ranks[parent] += self.ranks[child]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        unionfind = UnionFind(n)
        return all(unionfind.union(a, b) for a, b in edges)


# Union-Find
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(n):
            if n != parents[n]:
                parents[n] = find(parents[n])
            return parents[n]

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return False

            child, parent = (a, b) if ranks[a] < ranks[b] else (b, a)
            parents[child] = parent
            ranks[parent] += ranks[child]
            return True

        return all(union(a, b) for a, b in edges)


# DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        visit = [False] * n
        def dfs(i):
            if visit[i]:
                return False

            visit[i] = True
            for j in neighbors[i]:
                dfs(j)
            return True

        return dfs(0) and all(visit[i] for i in range(1, n))