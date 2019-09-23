class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        res=[]
        graph={}
        inD=[0]*numCourses
        for i in range(numCourses):
            graph[i]=[]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            inD[pair[0]]+=1

        while len(graph)>0:
            selnode=float("inf")
            for i in range(len(inD)):
                if inD[i]==0:
                    selnode=i
                    break
            res.append(selnode)
            if selnode==float("inf"):
                return []
            for node in graph[selnode]:
                inD[node]-=1
            del graph[selnode]
            inD[selnode]=float("inf")
        return res


a=Solution()

presp=[[1,0]]
num=2
print(a.canFinish(num,presp))

nums=2
psp=[[1,0],[0,1]]
print(a.canFinish(num,psp))