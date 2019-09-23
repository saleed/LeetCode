def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    row = [[0 for i in range(9)] for j in range(9)]
    col = [[0 for i in range(9)] for j in range(9)]
    box = [[0 for i in range(9)] for j in range(9)]
    bd=board
    print(row)

    for i in range(9):
        for j in range(9):
            if bd[i][j]!= '.':
                row[i][bd[i][j]]=1
                col[j][bd[i][j]]=1
                box[i/3*3+j/3][bd[i][j]]=1

    # sudu(0,0,row,col,box,bd)
    return

def sudu(i,j,row,col,box,bd):
    if i==9:
        print(bd)
        return
    if j==8:
        nexti=i+1
        nextj=0
    if bd[i][j]!='.':
        sudu(nexti, nextj, row, col, box, bd)
    boxid=i/3*3+j/3
    for d in range(1,9):
        if row[i][d]==1 or col[j][d]==1 or box[boxid][d]==1:
            continue
        else:
            row[i][d] = 1
            col[j][d] = 1
            box[boxid][d] = 1
            bd[i][j]=d
            sudu(nexti,nextj,row,col,box,bd)
            row[i][d] = 0
            col[j][d] = 0
            box[boxid][d] = 0
            bd[i][j]=0
    return

row = [[0 for i in range(9)] for j in range(9)]


def matrix():

    test=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

