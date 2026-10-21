class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        treasure = []
        steps = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    treasure.append((i, j))

        q = deque(treasure)

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for rd, cd in directions:
                    nr = row + rd
                    nc = col + cd
                    if (0<= nr < ROWS) and (0 <= nc < COLS) and (grid[nr][nc] == INF):
                        grid[nr][nc] = grid[row][col] + 1
                        q.append((nr, nc))
        
        