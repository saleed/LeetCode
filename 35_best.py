class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(len(board)):
            rowset = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowset:
                    return False
                else:
                    rowset.add(board[i][j])
        for j in range(len(board[0])):
            colset=set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in colset:
                    return False
                else:
                    colset.add(board[i][j])
        for i in range(9):
            px,py=(i/3)*3,i%3*3
            gridset=set()
            for p in range(3):
                for q in range(3):
                    if  board[px+p][py+q] ==".":
                        continue
                    if board[px+p][py+q] in gridset:
                        return False
                    else:
                        gridset.add(board[px+p][py+q])

        return True