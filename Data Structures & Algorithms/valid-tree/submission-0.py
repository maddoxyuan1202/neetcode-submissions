class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connect = {i: [] for i in range(n)}

        for node, edge in edges:
            connect[node].append(edge)
            connect[edge].append(node)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in connect[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n