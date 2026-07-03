class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = matrix[i][j]
                if i>0:
                    total += self.prefix[i-1][j]
                if j>0:
                    total += self.prefix[i][j-1]
                if i>0 and j>0:
                    total -= self.prefix[i-1][j-1]
                self.prefix[i][j] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tsum=self.prefix[row2][col2]
        if col1 > 0:
            tsum -= self.prefix[row2][col1-1]
        if row1 > 0:
            tsum -= self.prefix[row1-1][col2]
        if row1 > 0 and col1 > 0:
            tsum += self.prefix[row1-1][col1-1]
        return tsum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)