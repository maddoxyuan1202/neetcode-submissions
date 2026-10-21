class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        distances = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def dfs(r, c):
            if (min(r, c) < 0) or (r >= ROWS or c >= COLS) or (grid[r][c] != '1'):
                return 
            grid[r][c] = '0'
            for rd, cd in distances:
                dfs(r + rd, c + cd)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res