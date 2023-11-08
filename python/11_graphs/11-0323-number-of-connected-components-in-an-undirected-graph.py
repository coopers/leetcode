from typing import List


# Union-Find
# Time:  O(V + E ✖️ ⍺(V)) where V is the number of nodes
# Space: O(V)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n
        count = n
        
        def find(n):
            if n != parents[n]:
               parents[n] = find(parents[n])
            return parents[n]
        
        for i, j in edges:
            a, b = find(i), find(j)
            if a != b:
                child, parent = (a, b) if rank[a] < rank[b] else (b, a)
                parents[child] = parent
                rank[parent] += rank[child]
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


