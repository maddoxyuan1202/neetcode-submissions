class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for cur, pre in prerequisites:
            preMap[cur].append(pre)

        visit = set()

        def dfs(cur):
            if cur in visit:
                return False
            if preMap[cur] == []:
                return True

            visit.add(cur)
            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            
            visit.remove(cur)
            preMap[cur] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
