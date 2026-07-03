class NumArray:

    def __init__(self, nums: List[int]):
        self.PrefixSum = []
        total = 0
        for i in nums:
            total+=i
            self.PrefixSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        r = self.PrefixSum[right]
        if left > 0:
            l = self.PrefixSum[left-1]
        else:
            l = 0
        return r-l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)