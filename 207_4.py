class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


        deg={}
        for i in range(numCourses):
            deg[i]=[]
        for v in prerequisites:
            if v[0] in deg:
                deg[v[0]].append(v[1])
            else:
                deg[v[0]]=[v[1]]

        while True:
            if len(deg)==0:
                return True
            find=False
            node=-1
            for v in deg:
                if len(deg[v])==0:
                    find=True
                    node=v

            if find==False:
                return False
            else:
                for v in deg:
                    deg[v].remove(node)

