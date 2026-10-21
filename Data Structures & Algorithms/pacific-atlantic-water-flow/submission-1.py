class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS , COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        pac = set()
        alt = set()
        res = []

        def dfs(r, c, visited):
            if (r, c) in visited:
                return 
            
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

            return

        for c in range(COLS):
            dfs(0, c, pac)

        for r in range(ROWS):
            dfs(r, 0, pac)

        for c in range(COLS):
            dfs(ROWS-1, c, alt)
        for r in range(ROWS):
            dfs(r, COLS-1, alt)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in alt:
                    res.append((i, j))


        return res 