class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht={}
        ans=[]
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
            
        