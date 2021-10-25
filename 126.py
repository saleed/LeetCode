class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """






    def distance(self,word1,word2):
        if len(word1)!=len(word2):
            return 0
        distance=0
        for i in range(len(word1)):
            if word2[i]!=word1[i]:
                distance+=1
        return distance
    def bfs(self,begin,end,matrix,wordList):

        matrix = [[0 for _ in range(len(wordList))] for _ in range(len(wordList))]

        for i in range(len(wordList)):
            for j in range(len(wordList)):
                matrix[i][j] = self.distance(wordList[i], wordList[j])


        posMap={}
        for i in range(len(wordList)):
            posMap[wordList[i]]=i

        startPos=posMap[begin]
        endPos=posMap[end]
        queue=[startPos]
        preMap={startPos:None}
        distMap={startPos:0}
        vis=set()
        res=[]
        while len(queue)>0:
            head=queue[0]
            queue=queue[1:]
            vis.add(head)
            if head==endPos:
                p=head
                path=[endPos]
                while preMap[p]!=None:
                    path.append(preMap[head])
                    p=preMap[head]
            for j in range(len(matrix[head])):
                if matrix[head][j]==1 and distMap[j]










