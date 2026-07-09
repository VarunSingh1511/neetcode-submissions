class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        outp = []
        for i in nums:
            if i not in outp:
                outp.append(i)
        nums[:] = outp
        return len(nums)