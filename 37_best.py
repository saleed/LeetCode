import copy

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        colset=[set() for _ in range(len(board[0]))]
        rowset=[set() for _ in range(len(board))]
        gridset=[set() for _ in range(9)]





    def dfs(self,board,colset,rowset,gridset):
        x=-1
        y=-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    x=i
                    y=j
                    break

