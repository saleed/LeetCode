#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 14:23
# @Author  : sunaolin
# @File    : 36_4.py

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        srow=[set() for _ in range(9)]
        scol=[set() for _ in range(9)]
        tap=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                else:
                    if board[i][j] not in srow[i]:
                        srow[i].add(board[i][j])
                    else:
                        print(1, srow[i],i, j)
                        return False
                    if board[i][j] not in scol[j]:
                        scol[j].add(board[i][j])###########
                    else:
                        print(2, i, j)
                        return False
                    tapv=int(i/3)*3+int(j/3)
                    # print(board[i][j],tapv)
                    if board[i][j] not in tap[tapv]:
                        tap[tapv].add(board[i][j])
                    else:
                        # print(3, i, j)
                        return False
        return True

board =[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
a=Solution()
print(a.isValidSudoku(board))

for v in board:
    print(v)
