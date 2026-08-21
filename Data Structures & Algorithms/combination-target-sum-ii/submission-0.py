class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curComb = []
        candidates.sort()


        def dfs(i):
            if sum(curComb)>target:
                return
            
            if sum(curComb) == target:
                res.append(curComb.copy())
                return

            for j in range(i, len(candidates) ):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                curComb.append(candidates[j])
                dfs(j+1)
                curComb.pop()

        
        dfs(0)
        return res
