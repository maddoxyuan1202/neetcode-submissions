class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        distances = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = set()
        def dfs(r, c):
            if (min(r, c) < 0) or (r >= ROWS or c >= COLS) or (grid[r][c] == 0) or (r,c)  in visit:
                return 0
            visit.add((r, c))
            
            area = 1 + dfs(r + 1, c + 0) + dfs(r - 1, c + 0) + dfs(r + 0, c + 1) + dfs(r + 0, c - 1) 
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res