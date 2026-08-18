class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        curComb = []

        def dfs(i):
            if len(curComb) == k:
                comb.append(curComb.copy())
                return
            if i > n:
                return

            #include
            curComb.append(i)
            dfs(i+1)

            #not include
            curComb.pop()
            dfs(i+1)

        dfs(1)
        return comb