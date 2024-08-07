#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 17:29
# @Author  : sunaolin
# @File    : 130_3.py


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    res,vis=self.bfs(board,i,j)
                    if res==False:
                        for v in vis:
                            board[v[0]][v[1]]='X'
        # print(board)
        return board



    def bfs(self,board,i,j):
        que=[(i,j)]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        vis=set((i,j))
        res=False
        while len(que)>0:
            head=que[0]
            que=que[1:]
            # vis.add(head)  注意这里添加访问记录 会导致que中的数据重复
            if head[0]==0 or head[0]==len(board)-1 or head[1]==0 or head[1]==len(board[0])-1:
                res=True
            for s in range(4):
                ni=head[0]+dx[s]
                nj=head[1]+dy[s]
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj]=='O'and  (ni,nj) not in vis:
                    vis.add((ni,nj))
                    que.append((ni,nj))
        # print(res,vis)
        return res,vis


