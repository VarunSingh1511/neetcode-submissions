class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
    
        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r,c) in visited:
                return 0
            visited.add( (r,c) )
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return 1

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += dfs(i,j)

        return count
