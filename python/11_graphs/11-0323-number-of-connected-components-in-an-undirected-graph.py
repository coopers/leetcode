from typing import List


# Union Find With Rank
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        count = n
        
        def findParent(n):
            while n != parent[n]:
                n, parent[n] = parent[n], parent[parent[n]]
            return n
        
        for i, j in edges:
            p1, p2 = findParent(i), findParent(j)
            if p1 != p2:
                child, p = (p1, p2) if rank[p1] < rank[p2] else (p2, p1)
                parent[child] = p
                rank[p] += rank[child]
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

        return sum([dfs(i) for i in range(n)])
