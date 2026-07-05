class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cSum=0
        pSum = {0:1}
        for i in nums:
            cSum+=i
            diff = cSum - k
            res += pSum.get(diff,0)
            pSum[cSum] = 1 + pSum.get(cSum,0)
        return res
        