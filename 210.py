import Queue


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        notcylcle,path=self.canFinish(numCourses, prerequisites)
        if notcylcle==False:
            return []
        set1=set(path)
        set2=set(i for i in range(numCourses))
        print set1,set2,list(set2-set1),path
        path.extend(list(set2-set1))
        print path
        return path
        #
        # adjmtx = [[] for _ in range(numCourses)]
        # for pair in prerequisites:
        #     for id in range(1, len(pair)):
        #         adjmtx[pair[id]].append(pair[id - 1])
        # print adjmtx
        #
        # curpath = [0]
        # path = self.dfs(adjmtx, numCourses - 1, curpath)
        # if path != None and path[-1] == numCourses - 1:
        #     return curpath

    # we assume that there is no cycle in the graph,so use dfs is very simple

    # def dfs(self, adjmtx, end, curpath):
    #     if len(curpath) == 0:
    #         return
    #     curnode = curpath[-1]
    #     if curnode == end:
    #         return curpath
    #     for i in adjmtx[curnode]:
    #         curpath.append(i)
    #         ret = self.dfs(adjmtx, end, curpath)
    #         if ret != None:
    #             return curpath
    #         curpath.pop()
    #     return None

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjMtx = [[] for _ in range(numCourses)]
        print adjMtx[0]
        outD = [0] * numCourses

        for i in prerequisites:
            for j in range(1, len(i)):
                print j, i[j]
                adjMtx[i[j]].append(i[j - 1])
                outD[i[j - 1]] += 1
        que = Queue.deque()

        # print adjMtx
        for i in range(len(outD)):
            if outD[i] == 0:
                que.append(i)
        k = 0
        path=[]
        while que:
            print outD, adjMtx
            node = que.popleft()
            path.append(node)
            k += 1
            for i in adjMtx[node]:
                outD[i] -= 1
                if outD[i] == 0:
                    que.append(i)
        print k
        return k == numCourses,path




a=[1,2,3]
b=[]
a.extend(b)
print a