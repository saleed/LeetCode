import copy

rlt=0
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    chess=[['.' for i in range(n)] for j in range(n)]
    # print chess
    # print str(chess[0])
    col=[0 for i in range(n)]
    find(chess,col,0,n)
    return rlt



def find(chess,col,r,n):
    # print chess,r,n
    if r==n:
        return 1
    for c in range(n):
        if col[c]!=1 and duijiao(chess,r,c,n):
            chess[r][c]='Q'
            col[c]=1
            # print chess
            rlt=rlt+find(chess,col,r+1,n)
            col[c]=0
            chess[r][c]='.'
    return 0

def duijiao(chess,r,c,n):
    j=c-1
    i=r-1
    while j>=0 and i>=0:
        if chess[i][j]=='Q':
            return False
        i=i-1
        j=j-1
    j=c+1
    i=r-1
    while j<n and i>=0:
        if chess[i][j]=='Q':
            return False
        i=i-1
        j=j+1
    return True



print solveNQueens(4)



