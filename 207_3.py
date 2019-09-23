class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph={}
        indegree=[0]*numCourses
        for i in range(numCourses):
            graph[i]=[]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]]+=1

        res=[]
        while True:
            flag=0
            for node in range(len(indegree)):
                if indegree[node]==0:
                    indegree[node]=float("inf")
                    res.append(node)
                    for n in graph[node]:
                        indegree[n]-=1
                    del graph[node]
                    flag=1
                    break
            if flag==0:
                break
        return len(res)==numCourses




a=Solution()

presp=[[1,0]]
num=2
print(a.canFinish(num,presp))

nums=2
psp=[[1,0],[0,1]]
print(a.canFinish(num,psp))