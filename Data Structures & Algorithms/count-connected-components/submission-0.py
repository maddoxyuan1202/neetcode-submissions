class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        num = 0

        def dfs(node):
            for item in adj[node]:
                if visit[item]:
                    continue
                if not visit[item]:
                    visit[item] = True
                    dfs(item)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                num += 1

        return num