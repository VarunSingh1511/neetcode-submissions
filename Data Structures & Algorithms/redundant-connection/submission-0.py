class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}
        for v1,v2 in edges:
            if v1 not in adjList:
                adjList[v1] = []
            if v2 not in adjList:
                adjList[v2] = []
            adjList[v1].append(v2)
            adjList[v2].append(v1)


        visit = []
        cycle = set()
        def dfs(v,prev):
            if v in visit:
                idx = visit.index(v)
                for node in visit[idx:]:
                    cycle.add(node)
                return True

            visit.append(v)
            for v2 in adjList[v]:
                if v2 == prev:
                    continue
                if dfs(v2,v):
                    return True
            visit.pop()
            return False

        dfs(1,0)
        
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]

        return []