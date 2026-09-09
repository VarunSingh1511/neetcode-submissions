class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for crs,prq in prerequisites:
            adjList[crs].append(prq)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adjList[crs] == []:
                return True

            visit.add(crs)
            for prq in adjList[crs]:
                if not dfs(prq):
                    return False
            visit.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True