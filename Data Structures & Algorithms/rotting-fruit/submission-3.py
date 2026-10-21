class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        steps = -1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc  = row + dr, col + dc
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,  nc))

            steps += 1

        for row in grid:
            if 1 in row:
                return -1

        return max(0, steps)
        