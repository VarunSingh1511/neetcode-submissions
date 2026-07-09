class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        L,R = 0,0

        while R < n:
            nums[L]=nums[R]
            while R < n and nums[R]==nums[L]:
                R+=1
            L+=1
        
        return L
