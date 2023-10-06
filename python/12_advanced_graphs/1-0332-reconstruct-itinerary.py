from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        tickets.sort(reverse = True)
        edges = defaultdict(list)
        for src, des in tickets:
            edges[src].append(des),
        
        route = []
        def dfs(node):
            while edges[node]:
                dfs(edges[node].pop())
            route.append(node)

        dfs('JFK')
        return route[::-1]