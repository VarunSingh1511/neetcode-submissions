class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adjList = {i:[] for i in range(n)}
        for v1,v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        visited = set()

        def dfs(v, prev):
            if v in visited:
                return False
            visited.add(v)
            for v2 in adjList[v]:
                if v2 == prev:
                    continue
                if not dfs(v2, v):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        for i in range(n):
            if i not in visited:
                return False
        
        return True