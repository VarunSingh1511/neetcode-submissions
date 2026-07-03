class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prep=[]
        postp=[]
        n = len(nums)
        p1=1
        p2=1
        for i in range(n):
            p1*=nums[i]
            p2*=nums[n-i-1]
            prep.append(p1)
            postp.append(p2)
        postp.reverse()
        ans=[]
        for j in range(n):
            pro=1
            if j-1 >= 0 :
                pro*=prep[j-1]
            if j+1 < n:
                pro*=postp[j+1]
            ans.append(pro)
        return ans
