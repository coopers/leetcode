from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        edges = defaultdict(list)
        tickets.sort(reverse = True)
        for src, des in tickets:
            edges[src].append(des),
        
        route = []
        def dfs(node):
            while edges[node]:
                dfs(edges[node].pop())
            route.append(node)

        dfs('JFK')
        return route[::-1]