import queue

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """


        #权值为1的最短路问题，可以构造图求解，也可以使用BFS或DFS求解，
        # 感觉最短路问题其实都有BFS和DFS的思想在里面，想使用BFS进行求解，

        wordList.append(beginWord)
        wordList.append(endWord)
        adj=self.constructGraph(wordList)
        # notvis=set(wordList[:])
        mindepth={}
        for i in wordList:
            mindepth[i]=float("inf")
        mindepth[beginWord]=0  #为了找到所有的长度最小的路径，借助一个dict保存起点到其他节点的最小深度
        #使用BFS
        que=queue.Queue()
        que.put(beginWord)
        prenode={} #保存路径
        # for i in range(len(wordList)):
        #     prenode[i]=[]
        prenode[beginWord]="###"
        # notvis.remove(beginWord)
        res=[]
        print(adj)
        while not que.empty():
            tmp=que.get()
            if tmp==endWord:
                res.append(self.generatePath(prenode,endWord))
            if mindepth[tmp]>=mindepth[endWord]:  ###进一步剪枝
                continue
            for node in adj[tmp]:
                ###想不通怎么处理相同长度的路径
                if mindepth[node]>mindepth[tmp]+1:##注意这里的等于号！
                    mindepth[node]=mindepth[tmp]+1
                    que.put(node)
                    prenode[node]=[tmp]
                # elif mindepth[node]==mindepth[tmp]+1:
                #     que.put(node)
                #     prenode[node].append(tmp)
        return res




    def generatePath(self,prenode,endWord):
        node=endWord
        res=[]
        while node!="###":
            res.append(node)
            node=prenode[node]
        return list(reversed(res))


    def constructGraph(self,wordlist):
        dict={}
        for i in wordlist:
            dict[i]=[]
        for i in wordlist:
            for j in wordlist:
                if self.neighbour(i,j):
                    dict[i].append(j)
        return dict



    def neighbour(self,w1,w2):
        count=0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                count+=1
        return count==1


a=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(a.findLadders(beginWord,endWord,wordList))




#无记忆的DFS超时，
# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         if endWord not in wordList:
#             return []
#         newlist=wordList[:]
#         newlist.append(beginWord)
#         newlist.append(endWord)
#
#         start=0
#         end=0
#
#         newlist=list(set(newlist))
#         for i in range(len(newlist)):
#             if newlist[i]==beginWord:
#                 start=i
#             elif newlist[i]==endWord:
#                 end=i
#
#         print newlist,start,end
#         distmtx=[[0 for _ in range(len(newlist))] for _ in range(len(newlist))]
#
#         for i in range(len(newlist)):
#             for j in range(len(newlist)):
#                 if self.calDist(newlist[i],newlist[j])==1:
#                     distmtx[i][j]=1
#                     distmtx[j][i]=1
#
#         for i in range(len(newlist)):
#             print distmtx[i]
#
#         path=[start]
#         vis=[0]*len(newlist)
#         res=[]
#         self.dfs(distmtx,end,res,vis,path)
#         minlen=float("inf")
#         result=[]
#         for i in res:
#             minlen=min(len(i),minlen)
#         for i in res:
#             if len(i)==minlen:
#                 result.append(i)
#
#         strlist=[]
#         for lst in result:
#             cur=[]
#             for i in lst:
#                 cur.append(newlist[i])
#             strlist.append(cur)
#             print cur
#         return strlist
#
#     def dfs(self,mtx,end,res,vis,path):
#         if path[-1]==end:
#             # print "######",path,path[-1]
#             newpath = copy.deepcopy(path)
#             if len(res)>0:
#                 if len(res[0])>len(path):
#                     res[:]=[newpath]  ### be careful for this redefine a value of res
#                     return
#             res.append(newpath)
#             return
#         curnode=path[-1]
#         if len(res)>0 and len(path)>=len(res[0]):
#             return
#         for i in range(len(mtx[0])):
#             if vis[i]==0 and mtx[curnode][i]==1:
#                 vis[i]=1
#                 path.append(i)
#                 self.dfs(mtx,end,res,vis,path)
#                 vis[i]=0
#                 path.pop()
#
#
#     def calDist(self,a,b):
#         if len(a)!=len(b):
#             return 0
#         if a==b:
#             return 0
#         dist=0
#         for i in range(len(a)):
#             if a[i]!=b[i]:
#                 dist+=1
#         return dist