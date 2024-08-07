#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 19:53
# @Author  : sunaolin
# @File    : 51_5.py


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        colset=set()
        board=[['.' for _ in range(n)] for _ in range(n)]
        res=[]
        self.dfs(board,0,colset,res,n)
        return res

    def dfs(self,board,i,colset,res,n):
        # print(colset)
        # print(board)

        if i==n:
            tmpres=[]
            for v in board:
                tmpres.append("".join(v))
            res.append(copy.deepcopy(tmpres))
            return
        for j in range(len(board[0])):
            if j not in colset and self.checkAngle(i,j,board):
                colset.add(j)
                board[i][j]='Q'
                self.dfs(board,i+1,colset,res,n)
                board[i][j] = '.'
                colset.remove(j)

    def checkAngle(self,x,y,board):
        i=x
        j=y

        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            print(i,j)
            i-=1
            j-=1

        i = x
        j = y
        while i >= 0 and j <len(board[0]):
            if board[i][j] == 'Q':
                return False
            print(i,j)
            i -= 1
            j += 1
        return True
#
#
# board=[['.' for _ in range(4)] for _ in range(4)]
# checkAngle(2,0,board)