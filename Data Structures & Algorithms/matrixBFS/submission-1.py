class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        def bfs(grid):
            ROWS = len(grid)
            COLS = len(grid[0])
            visit = set()
            queue = deque()
            if grid[0][0]==1:
                return -1
            queue.append((0,0))
            visit.add((0,0))

            length = 0


            def travel(r,c):
                if min(r,c) < 0 or r==ROWS or c==COLS or (r,c) in visit or grid[r][c] == 1:
                    return 
                queue.append((r,c))
                visit.add((r,c))        

            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    if r == ROWS - 1 and c == COLS - 1:
                        return length

                    travel(r+1,c)
                    travel(r-1,c)
                    travel(r,c+1)
                    travel(r,c-1)

                length += 1
                    
            return -1

        return(bfs(grid))