from typing import List


# Union-Find
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            while n != parent[n]:
                n, parent[n] = parent[n], parent[parent[n]]
            return n

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            child, p = (p1, p2) if rank[p1] < rank[p2] else (p2, p1)
            parent[child] = p
            rank[p] += rank[child]
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

        if not dfs(0):
            return False
        
        return all(visit[i] for i in range(n))