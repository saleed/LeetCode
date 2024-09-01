#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/14 16:24
# @Author  : sunaolin
# @File    : 723_1.py

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        while True:
            crush,flag=self.crushCandy(board)
            print(crush,flag)
            if flag==False:
                return board
            for j in range(len(board[0])):
                cnt=0
                for i in range(len(board))[::-1]:
                    if (i,j) in crush:
                        cnt+=1
                    else:
                        board[i+cnt][j]=board[i][j]
                for i in range(cnt):
                    board[i][j]=0




    def crushCandy(self,board):
        res=set()
        flag=True


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    continue
                k=i+1
                while k<len(board) and board[k][j]==board[i][j]:
                    k+=1
                if k-i>=3:
                    for s in range(i,k):
                        res.add((s,j))

                k = i -1
                while k>=0 and board[k][j] == board[i][j]:
                    k -= 1
                if i-k>= 3:
                    for s in range(k+1,i+1):
                        res.add((s,j))

                k = j + 1
                while k < len(board[0]) and board[i][k] == board[i][j]:
                    k+=1
                if k - j >= 3:
                    for s in range(j,k):
                        res.add((i,s))

                k = j-1
                while k>=0 and board[i][k] == board[i][j]:
                    k-=1
                if j-k >= 3:
                    for s in range(k+1,j+1):
                        res.add((i,s))

                # print(i,j,res)
        if len(res)==0:
            flag=False
        return res,flag











