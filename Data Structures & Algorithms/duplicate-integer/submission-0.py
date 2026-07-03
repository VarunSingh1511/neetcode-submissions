class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht={}
        for i in nums:
            if i in ht :
                ht[i] += 1
            else:
                ht[i]=1
        for j in ht:
            if ht[j]>1:
                return True
        return False