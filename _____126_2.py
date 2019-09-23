##其实就已经转换成了最短路径的问题

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        newlist=wordList[:]
        newlist.append(beginWord)
        newlist.append(endWord)

        start=0
        end=0

        newlist=list(set(newlist))
        for i in range(len(newlist)):
            if newlist[i]==beginWord:
                start=i
            elif newlist[i]==endWord:
                end=i

        print newlist,start,end
        distmtx=[[0 for _ in range(len(newlist))] for _ in range(len(newlist))]

        for i in range(len(newlist)):
            for j in range(len(newlist)):
                if self.calDist(newlist[i],newlist[j])==1:
                    distmtx[i][j]=1
                    distmtx[j][i]=1

        for i in range(len(newlist)):
            print distmtx[i]


        path=[start]
        vis=[0]*len(newlist)
        res=[]
        self.dfs(distmtx,end,res,vis,path)
        minlen=float("inf")
        result=[]
        for i in res:
            minlen=min(len(i),minlen)
        for i in res:
            if len(i)==minlen:
                result.append(i)

        strlist=[]
        for lst in result:
            cur=[]
            for i in lst:
                cur.append(newlist[i])
            strlist.append(cur)
            print cur
        return strlist



    def dfs(self,mtx,end,res,vis,path):
        if path[-1]==end:
            # print path,path[-1]
            newpath=copy.deepcopy(path)
            res.append(newpath)
        curnode=path[-1]

        for i in range(len(mtx[0])):
            if vis[i]==0 and mtx[curnode][i]==1:
                vis[i]=1
                path.append(i)
                self.dfs(mtx,end,res,vis,path)
                vis[i]=0
                path.pop()


    def calDist(self,a,b):
        if len(a)!=len(b):
            return 0
        if a==b:
            return 0
        dist=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                dist+=1
        return dist
