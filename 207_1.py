class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adjMat=[[0  for i in range(numCourses)] for _ in range(numCourses)]
        for v in prerequisites:
            adjMat[v[0]][v[1]]=1

        deg={}


        for i in range(numCourses):
            deg[i]=0
            for j in range(numCourses):
                if adjMat[j][i]==1:
                    deg[i]+=1

        while True:
            if len(deg)==0:
                return True
            id=-1
            for i in range(len(deg)):
                if deg[i]==0:
                    id=i
                    break
            if id==-1:
                return False

            for i in range(numCourses):
                if adjMat[id][i]==1:
                    deg[i]-=1
            del deg[id]









