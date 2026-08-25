class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        COL = set()
        posDIAG = set()
        negDIAG = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                bCopy = ["".join(row) for row in board]
                res.append(bCopy)
                return

            for c in range(n):
                if c in COL or (r + c) in posDIAG or (r - c) in negDIAG:
                    continue
                
                COL.add(c)
                posDIAG.add(r + c)
                negDIAG.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                COL.remove(c)
                posDIAG.remove(r + c)
                negDIAG.remove(r - c)
                board[r][c] = "."

        
        backtrack(0)
        return res