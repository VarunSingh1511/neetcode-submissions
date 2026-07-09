class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        outp = []
        ht ={}
        for i in nums:
            if i not in ht:
                ht[i]=1
                outp.append(i)
        nums[:] = outp
        return len(nums)