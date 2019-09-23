import Queue
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjMtx=[[] for _ in range(numCourses)]
        print adjMtx[0]
        outD=[0]*numCourses

        for i in prerequisites:
            for j in range(1,len(i)):
                print j,i[j]
                adjMtx[i[j]].append(i[j-1])
                outD[i[j-1]]+=1
        que=Queue.deque()
        # print adjMtx
        for i in range(len(outD)):
            if outD[i]==0:
                que.append(i)
        k=0
        while que:
            print outD,adjMtx
            node=que.popleft()
            k+=1
            for i in adjMtx[node]:
                outD[i]-=1
                if outD[i]==0:
                    que.append(i)
        print k
        return k==numCourses


n=2
p=[[1,0]]



a=Solution()
# Output: "9534330"
print a.canFinish(n,p)




