import queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """


        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        # wordList.append(endWord)

        # notvis=set(wordList[:])
        # prenode={} #保存路径
        # for i in range(len(wordList)):
        #     prenode[i]=[]
        # prenode[beginWord]="###"
        # notvis.remove(beginWord)
        # res=[]
        # print(adj)

        return self.bfs2(beginWord,endWord,wordList)


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
            if count>1:
                return False
        return count==1


    def bfs1(self,beginWord,endWord,wordList):
        mindepth={}
        for i in wordList:
            mindepth[i]=float("inf")
        mindepth[beginWord]=0  #为了找到所有的长度最小的路径，借助一个dict保存起点到其他节点的最小深度
        #使用BFS
        adj=self.constructGraph(wordList)
        que=queue.Queue()
        que.put(beginWord)
        while not que.empty():
            tmp = que.get()
            if tmp == endWord:
                # res.append(self.generatePath(prenode,endWord))
                return mindepth[tmp]
            if mindepth[tmp] >= mindepth[endWord]:  ###进一步剪枝
                continue
            for node in adj[tmp]:
                ###想不通怎么处理相同长度的路径
                if mindepth[node] > mindepth[tmp] + 1:  ##注意这里的等于号！
                    mindepth[node] = mindepth[tmp] + 1
                    que.put(node)
                    # prenode[node]=[tmp]
                # elif mindepth[node]==mindepth[tmp]+1:
                #     que.put(node)
                #     prenode[node].append(tmp)
        return 0


    def bfs2(self,beginWord,endWord,wordList):
        mindepth={}
        for i in wordList:
            mindepth[i]=0
        mindepth[beginWord]=1  #为了找到所有的长度最小的路径，借助一个dict保存起点到其他节点的最小深度
        #使用BFS
        adj=self.constructGraph(wordList)
        que=queue.Queue()
        que.put(beginWord)
        vis=set()
        vis.add(beginWord)
        while not que.empty():
            tmp = que.get()
            if tmp == endWord:
                # res.append(self.generatePath(prenode,endWord))
                break
            for node in adj[tmp]:
                ###想不通怎么处理相同长度的路径
                if node in vis:
                    continue
                mindepth[node] = mindepth[tmp] + 1
                que.put(node)
                vis.add(node)
                    # prenode[node]=[tmp]
                # elif mindepth[node]==mindepth[tmp]+1:
                #     que.put(node)
                #     prenode[node].append(tmp)
        # print(mindepth)
        return mindepth[endWord]


a=Solution()


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(a.ladderLength(beginWord,endWord,wordList))



beginWord= "hit"
endWord = "cog"
wordList =["hot","dot","dog","lot","log"]
print(a.ladderLength(beginWord,endWord,wordList))

