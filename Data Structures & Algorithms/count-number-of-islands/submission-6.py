class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(r, c):
            if (min(r, c) < 0) or (r >= ROWS or c >= COLS) or (grid[r][c] == '0'):
                return False
            grid[r][c] = '0'
            for direction in directions:
                dfs(r+direction[0], c+direction[1])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands