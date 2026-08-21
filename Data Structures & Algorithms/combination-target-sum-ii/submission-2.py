class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curComb = []
        candidates.sort()


        def dfs(i):
            if sum(curComb) == target:
                res.append(curComb.copy())
                return

            if sum(curComb)>target or i == len(candidates):
                return
            
    
            curComb.append(candidates[i])
            dfs(i+1)
            curComb.pop()

            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1)
            
        
        dfs(0)
        return res
