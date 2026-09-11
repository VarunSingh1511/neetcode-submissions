class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {c:[] for c in range(numCourses)}
        for crs,prq in prerequisites:
            adjList[crs].append(prq)

        visiting, visited = set(), set()
        res = []
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for prq in adjList[crs]:
                if not dfs(prq):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if c not in visited:
                if not dfs(c):
                    return []

        return res
