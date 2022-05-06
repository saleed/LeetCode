class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """




    def bfs(self,board,hand):
        que=[board]
        dist={}

        while len(que)>0:
            if "" in dist:
                return dist[""]
            head=que[0]
            que=que[1:]
            if head in dist:
                continue
            if len(hand)==0:
                break
            else:
                han
                for i in range(len(hand)):
                    newstr=hand[-1]


        if len(board)==0
        if board in vis:




