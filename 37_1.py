class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rowset = []
        colset = []
        gridset = []
        digit = set()

        for i in range(9):
            rowset.append(set())
            colset.append(set())
            gridset.append(set())
            digit.add(str(i+1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    rowset[i].add(str(board[i][j]))
                    colset[j].add(str(board[i][j]))
                    gridset[(i / 3) * 3 + j / 3].add(str(board[i][j]))


        if self.dfs(board,rowset,colset,gridset,digit,0,0):
            return board
        return None



    def dfs(self,board,rowset,colset,gridset,digit,i,j):
        if i>=9:
            return True
        if j==8:
            nexti=i+1
            nextj=0
        else:
            nexti=i
            nextj=j+1
        if board[i][j]==".":
            for s in range(1,10):
                if self.checkVailid(rowset,colset,gridset,digit,i,j,str(s)):
                    # print(board)
                    board[i][j]=str(s)
                    rowset[i].add(str(s))
                    colset[j].add(str(s))
                    gridset[(i/3)*3+j/3].add(str(s))
                    if self.dfs(board,rowset,colset,gridset,digit,nexti,nextj):
                        return True
                    else:
                        board[i][j] = "."
                        rowset[i].remove(str(s))
                        colset[j].remove(str(s))
                        gridset[(i / 3) * 3 + j / 3].remove(str(s))

            return False
        else:
            if self.dfs(board,rowset,colset,gridset,digit,nexti,nextj):
                return True
            else:
                return False

    def checkVailid(self,rowset,colset,gridset,digit,i,j,s):
        row = i
        col = j
        grid = (i / 3) * 3 + j / 3
        # print(i,j,row,col,grid,board[i][j],rowset,colset,gridset)
        if s in digit:
            if s in rowset[row] or s in colset[col] or s in gridset[grid]:
                return False
        return True

if __name__ == "__main__":
    a=Solution()
    test=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(a.solveSudoku(test))
    # print(test)

