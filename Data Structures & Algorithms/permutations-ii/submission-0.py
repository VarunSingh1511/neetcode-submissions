class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        Perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(Perm) == len(nums):
                res.append(Perm.copy())
                return
            
            for n in count:
                if count[n]>0:
                    Perm.append(n)
                    count[n] -= 1

                    dfs()

                    Perm.pop()
                    count[n] += 1
        
        dfs()
        return res