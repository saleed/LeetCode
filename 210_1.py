class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adjMat = [[0 for i in range(numCourses)] for _ in range(numCourses)]
        for v in prerequisites:
            adjMat[v[1]][v[0]] = 1

        deg = {}

        for i in range(numCourses):
            deg[i] = 0
            for j in range(numCourses):
                if adjMat[j][i] == 1:
                    deg[i] += 1

        res = []

        while True:
            if len(deg) == 0:
                break
            id = -1
            for i in deg:
                if deg[i] == 0:
                    id = i
                    break
            if id == -1:
                return []

            for i in range(numCourses):
                if adjMat[id][i] == 1:
                    deg[i] -= 1

            res.append(id)
            del deg[id]

        return res







