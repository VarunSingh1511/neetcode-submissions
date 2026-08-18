class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        curComb = []

        def dfs(i):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return
            elif sum(curComb) > target:
                return

            for j in range(i , len(nums)):
                curComb.append(nums[j])
                dfs(j)
                curComb.pop()

        dfs(0)
        return combs