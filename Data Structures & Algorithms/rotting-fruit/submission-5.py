class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        def travel(r, c):
            nonlocal fresh
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return
            queue.append((r, c))
            grid[r][c]=2
            fresh -= 1

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                travel(r + 1, c)
                travel(r - 1, c)
                travel(r, c + 1)
                travel(r, c - 1)
            time += 1

        return time if fresh == 0 else -1