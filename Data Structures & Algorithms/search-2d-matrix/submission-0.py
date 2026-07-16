class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m =  len(matrix)
        n = len(matrix[0])
        
        l1,r1=0,m-1

        while l1 <= r1:
            l2,r2=0,n-1
            mid = (l1 + r1)//2

            if target > matrix[mid][-1]:
                l1 = mid + 1
            elif target < matrix[mid][0]:
                r1 = mid - 1
            else:
                while l2 <= r2:
                    mid2 = (l2 + r2)//2
                    if target > matrix[mid][mid2]:
                        l2 = mid2 + 1
                    elif target < matrix[mid][mid2]:
                        r2 = mid2 - 1
                    else:
                        return True
                return False

        return False