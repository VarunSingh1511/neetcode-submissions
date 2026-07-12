class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minlen = n+1
        l = 0
        total=0
        for r in range(n):
            total+= nums[r]
            while total>=target:
                minlen = min(minlen, r-l+1)
                total-=nums[l]
                l+=1
        return 0 if minlen == n+1 else minlen