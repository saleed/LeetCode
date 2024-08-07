#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 14:08
# @Author  : sunaolin
# @File    : 529_1.py

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        self.bfs(board,click[0],click[1])
        return board


    def bfs(self,board,x,y):
        if board[x][y]=="M":
            board[x][y]="X"
            return

        que=[(x,y)]
        board[x][y] = "B"
        cnt=self.aroundMineNum(board,x,y)
        if cnt:
            board[x][y] =str(cnt)
            return


        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        while len(que)>0:
            head=que[0]
            que=que[1:]

            for i in range(8):
                nx=head[0]+dx[i]
                ny=head[1]+dy[i]
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny]=="E":
                    cnt=self.aroundMineNum(board,nx,ny)
                    ##检测到相邻的
                    if cnt==0:
                        que.append((nx,ny))
                        board[nx][ny]="B"
                    else:
                        board[nx][ny]=str(cnt)





    def aroundMineNum(self,board,x,y):
        dx=[1,1,0,-1,-1,-1,0,1]
        dy=[0,1,1,1,0,-1,-1,-1]
        cnt=0
        print(x,y)
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny]=="M":
                cnt+=1
        return cnt


board =[["E","M","M","2","B","B","B","B"],["E","E","M","2","B","B","B","B"],["E","E","2","1","B","B","B","B"],["E","M","1","B","B","B","B","B"],["1","2","2","1","B","B","B","B"],["B","1","M","1","B","B","B","B"],["B","1","1","1","B","B","B","B"],["B","B","B","B","B","B","B","B"]]

for v in board:
    print(v)
click =[0,0]
a=Solution()
a.updateBoard(board,click)
print("   ")
for v in board:
    print(v)
