class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rowset=[]
        colset=[]
        gridset=[]

        digit=set()


        for i in range(9):
            rowset.append(set())
            colset.append(set())
            gridset.append(set())
            digit.add(str(i+1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                row=i
                col=j
                grid=(i/3)*3+j/3
                # print(i,j,row,col,grid,board[i][j],rowset,colset,gridset)
                if board[i][j] in digit:
                    if board[i][j] in rowset[row] or board[i][j] in colset[col] or board[i][j] in gridset[grid]:
                        return False

                    rowset[row].add(board[i][j])
                    colset[col].add(board[i][j])
                    gridset[grid].add(board[i][j])
        return True


if __name__=="__main__":
    a=Solution()
    board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(a.isValidSudoku(board))
