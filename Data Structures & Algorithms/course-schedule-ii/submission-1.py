class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        res = []
        visit = set()
        visited = set()
        for crs, prq in prerequisites:
            adjList[crs].append(prq)

        def dfs(crs):
            if crs in visit:
                return False 
            if crs in visited:
                return True

            visit.add(crs)
            for prq in adjList[crs]:
                if not dfs(prq):
                    return False
            visit.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
    
        return res