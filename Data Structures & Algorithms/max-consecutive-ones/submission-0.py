class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        con = 0
        maxc = 0
        for i in range(n):
            if nums[i] == 1:
                con += 1
            else:
                if con > maxc:
                    maxc=con
                con = 0
        if con > maxc:
            maxc = con
        return maxc
            