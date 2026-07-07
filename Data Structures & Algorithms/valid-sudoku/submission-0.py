class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hasht={}
        hasht2={}
        for z in range(9):
            hasht[z]=[]
        for z in range(9):
            hasht2[z]=[]
        for i in range(9):
            visited = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in visited or board[i][j] in hasht[j]:
                    return False
                visited.append(board[i][j])
                hasht[j].append(board[i][j])
                
                a=int(i/3)
                b=int(j/3)
                idx = 3*a + b
                hasht2[idx].append(board[i][j])
                    
        for i in range(9):
            arr2 = hasht2[i]
            visited2=[]
            for j in arr2:
                if j in visited2:
                    return False
                visited2.append(j)
                
        return True       
                
                
                
                
