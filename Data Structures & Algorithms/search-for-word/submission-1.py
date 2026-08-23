class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(idx,i,j):

            if idx == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[idx] != board[i][j]:
                return False    

      
            temp = board[i][j]
            board[i][j] = "#"
            
            if (dfs(idx + 1, i, j-1 ) or 
                dfs(idx + 1, i, j+1 ) or 
                dfs(idx + 1, i+1, j ) or 
                dfs(idx + 1, i-1, j )):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True

        return False