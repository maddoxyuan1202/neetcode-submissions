class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        num = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visit[node] = True
            for item in adj[node]:     
                if not visit[item]:
                    visit[item] = True 
                    dfs(item)

        
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                num += 1
        
        return num