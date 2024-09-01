#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 18:05
# @Author  : sunaolin
# @File    : 794.py


class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        num1=0
        num2=0
        for i  in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="X":
                    num1+=1
                elif board[i][j]=="O":
                    num2+=1
        print(num1,num2)
        print(self.win(board,1),self.win(board,2))
        if (num1-num2==0 and not self.win(board,1)) or (num1-num2==1 and not self.win(board,2)):
            return True
        return False



    def win(self,board,role):
        if role==1:
            c="X"
        else:
            c="O"

        if board[0]==c*3 or board[1]==c*3 or board[2]==c*3:
            return True
        if (board[0][0]==c and board[1][0]==c and board[2][0]==c) or (board[0][1] == c and board[1][1] == c and board[2][2] == c) or (board[0][2] == c and board[1][2] == c and board[2][2] == c):
            return True
        if (board[0][0]==c and board[1][1]==c and board[2][2]==c):
            return True
        return False
