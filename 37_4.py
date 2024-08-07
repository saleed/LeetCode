#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 15:01
# @Author  : sunaolin
# @File    : 37_4.py

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        s,c,t=self.getSet(board)  ###
        print(s)
        print(c)
        print(t)
        res=[]
        print(self.dfs(board,0,0,res,s,c,t))
        return res

    def getSet(self,board):
        srow = [set() for _ in range(9)]
        scol = [set() for _ in range(9)]
        tap = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] not in srow[i]:
                        srow[i].add(board[i][j])
                    if board[i][j] not in scol[j]:
                        scol[j].add(board[i][j]) ####这里写成了scol[i]
                    tapv = int(i / 3) * 3 + int(j / 3)
                    if board[i][j] not in tap[tapv]:
                        tap[tapv].add(board[i][j])
        return srow,scol,tap

    def dfs(self,board,x,y,res,rowset,colset,aset):
        # print(x,y)
        # print(board)
        # print(rowset[x])
        # print(rowset[y])

        if x==9:
            # print(board)
            res.append(board[:][:])
            return True
        if y==8:
            # print(888)
            # print(board[0])
            nx=x+1
            ny=0
            # print(nx,ny)
        else:
            nx=x
            ny=y+1
        v = int(x / 3) * 3 + int(y / 3)
        # print(rowset[v])
        if board[x][y]==".":
            # print(1)
            for i in range(1,10):
                if str(i) not in rowset[x] and str(i) not in colset[y] and str(i) not in aset[v]:
                    # print("gggg",i)
                    rowset[x].add(str(i))
                    colset[y].add(str(i))
                    aset[v].add(str(i))
                    board[x][y]=str(i)
                    if self.dfs(board,nx,ny,res,rowset,colset,aset):
                        return True
                    board[x][y] ="."
                    rowset[x].remove(str(i))
                    colset[y].remove(str(i))
                    aset[v].remove(str(i))
        else:
            if self.dfs(board, nx, ny, res, rowset, colset, aset):
                return True
        return False


