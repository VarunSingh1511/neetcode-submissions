class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n

        while l<=r:
            mid = (l+r)//2
            res = guess(mid)
            if res == 1:
                l = mid + 1
            elif res == -1:
                r = mid - 1
            else:
                return mid
        
        return -1