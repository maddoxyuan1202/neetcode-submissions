class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for cur, pre in prerequisites:
            preMap[cur].append(pre)

        visited = set()
        completed = set()
        res = []

        def dfs(cur):
            if cur in visited:
                return False
            if cur in completed:
                return True

            visited.add(cur)

            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            visited.remove(cur)
            completed.add(cur)
            res.append(cur)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res