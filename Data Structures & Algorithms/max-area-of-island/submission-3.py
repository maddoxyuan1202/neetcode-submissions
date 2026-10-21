class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islandsArea = 0
        res = 0
        def dfs(r, c):
            if (min(r,c)< 0) or (r >= ROWS or c >= COLS) or grid[r][c] == 0:
                return 0
            nonlocal islandsArea
            islandsArea += 1
            grid[r][c] = 0
            for rd, cd in directions:
                dfs(r+rd, c+cd)
            return islandsArea
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    islandsArea = 0
                    res = max(res,dfs(i,j))
        
        return res
            