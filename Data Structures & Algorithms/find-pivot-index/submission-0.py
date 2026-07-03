class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        presum=[]
        postsum=[]
        pre=0
        post=0
        for i in range(n):
            pre+=nums[i]
            post+=nums[n-i-1]
            presum.append(pre)
            postsum.append(post)
        postsum.reverse()
        print(presum)
        print(postsum)
        for j in range(n):
            if presum[j] == postsum[j]:
                return j
        return -1
    
    

