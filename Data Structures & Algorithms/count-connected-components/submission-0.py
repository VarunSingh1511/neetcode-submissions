class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        for v1,v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visit = set()
        def dfs(v,prev):
            if v in visit:
                return
            visit.add(v)
            for v2 in adjList[v]:
                if v2 == prev:
                    continue
                dfs(v2,v)
            
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                count+=1
        return count