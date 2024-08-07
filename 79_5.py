#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/24 19:44
# @Author  : sunaolin
# @File    : 79_5.py

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word=="":
            return True

        vis=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word,board,i,j,vis):
                    return True
        return False


    def dfs(self,word,board,i,j,vis):
        if word=="":
            return True

        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for d in range(4):
            ni=i+dx[d]
            nj=j+dy[d]
            if 0<=ni<len(board) and 0<=nj<len(board[0]) and (ni,nj) not in vis and board[ni][nj]==word[0]:
                vis.add((ni,nj))
                res=self.dfs(word[1:],board,ni,nj,vis)
                vis.remove((ni,nj))
                if res:
                    return True
        return False







