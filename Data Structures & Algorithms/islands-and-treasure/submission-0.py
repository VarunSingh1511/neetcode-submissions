class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        def travel(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == -1 or grid[r][c] == 0 or (r,c) in visit:
                return
            queue.append((r,c))
            visit.add((r,c))
        def bfs():
            dist = 0
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    grid[r][c] = dist
                    travel(r+1,c)
                    travel(r-1,c)
                    travel(r,c+1)
                    travel(r,c-1)

                dist += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visit.add((i,j))

        bfs()
        return   

        
