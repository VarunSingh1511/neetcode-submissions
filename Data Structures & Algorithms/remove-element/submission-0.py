class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        cntr = 0
        i = 0
        while i < n:

            if nums[i]==val:
                for idx in range(i,n-1):
                    nums[idx] = nums[idx+1]
                n -= 1
                nums[n] = 0

            else:
                cntr += 1
                i+=1

        return cntr