class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        def countComponents(skip):
            adj = [[] for _ in range(n + 1)]

            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue

                adj[u].append(v)
                adj[v].append(u)

            visited = set()

            def dfs(node):
                visited.add(node)

                for nei in adj[node]:
                    if nei not in visited:
                        dfs(nei)

            num = 0

            for i in range(1, n + 1):
                if i not in visited:
                    dfs(i)
                    num += 1

            return num


        for i in range(len(edges) - 1, -1, -1):
            if countComponents(i) == 1:
                return edges[i]

        return []
