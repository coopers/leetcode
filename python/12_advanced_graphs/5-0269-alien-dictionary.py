from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            b = True
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    b = False
                    break
            if b and len(w1) > len(w2):
                return ''

        remaining = {char for char in adj}
        current = set()
        res = []

        def dfs(char):
            remaining.remove(char)
            current.add(char)
            for nextChar in adj[char]:
                if nextChar in current or (nextChar in remaining and dfs(nextChar)):
                    return True
                
            current.remove(char)
            res.append(char)

        for char in adj:
            if char in remaining and dfs(char):
                return ''

        res.reverse()
        return ''.join(res)


class Solution:
    def add_words_to_graph(self, graph, w1, w2):
        min_length = min(len(w1), len(w2))
        for i in range(min_length):
            if w1[i] != w2[i]:
                graph[w1[i]].add(w2[i])
                return True

        return len(w1) <= len(w2)

    def topo_dfs(self, x, g, visited, visiting, st):
        visited.add(x)
        visiting.add(x)
        for nbr in g[x]:
            if nbr in visiting:
                return True
            if nbr not in visited:
                if self.topo_dfs(nbr, g, visited, visiting, st):
                    return True
        
        visiting.remove(x)
        st.append(x)
        return False

    def alienOrder(self, words):
        graph = {char: set() for word in words for char in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if not self.add_words_to_graph(graph, w1, w2):
                return ''
            
        visited, visiting, st = set(), set(), []
        for k in graph.keys():
            if k not in visited:
                if self.topo_dfs(k, graph, visited, visiting, st):
                    return ''
                
        st.reverse()
        return ''.join(st)