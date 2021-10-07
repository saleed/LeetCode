import copy

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        res=[]

        rowset=[]
        colset=[]
        gridset=[]

        for i in range(9):
            rowset.append(set())
            colset.append(set())
            gridset.append(set())

        for i in range(len(board)):
            for j in range(len(board[0])):
                grid = (i / 3) * 3 + j / 3
                if board[i][j]==".":
                    continue

                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                gridset[grid].add(board[i][j])

        print(rowset)
        print(colset)
        print(gridset)
        if self.dfs(board,res,rowset,colset,gridset):
            return res
        return None

    def dfs(self,board,res,rowset,colset,gridset):
        x=-1
        y=-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    x=i
                    y=j
                    break

        if x == -1 and y == -1:
            res.append(copy.deepcopy(board[:][:]))
            return True
        grid = (x/ 3) * 3 + y / 3
        for v in range(1,10):
            board[x][y]=str(v)
            if str(v) in rowset[x] or str(v) in colset[y] or str(v) in gridset[grid]:
                continue
            # print(i,j,row,col,grid,board[i][j],rowset,colset,gridset)

            rowset[x].add(str(v))
            colset[y].add(str(v))
            gridset[grid].add(str(v))
            if self.dfs(board,res,rowset,colset,gridset):
                return True

            board[x][y] = "."
            rowset[x].remove(str(v))
            colset[y].remove(str(v))
            gridset[grid].remove(str(v))

        return False




if __name__ == "__main__":
    a=Solution()
    test=[[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
    print(a.solveSudoku(test))
    # print(test)


