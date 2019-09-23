import copy

def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    chess=[['.' for i in range(n)] for j in range(n)]
    # print chess
    # print str(chess[0])
    col=[0 for i in range(n)]
    rlt=[]
    find(chess,col,0,n,rlt)
    rlt=postprocess(rlt)
    return rlt


def find(chess,col,r,n,rlt):
    # print chess,r,n
    if r==n:
        # print chess
        newchess=copy.deepcopy(chess)
        rlt.append(postprocess(newchess))
        return
    for c in range(n):
        if col[c]!=1 and duijiao(chess,r,c,n):
            chess[r][c]='Q'
            col[c]=1
            # print chess
            find(chess,col,r+1,n,rlt)
            col[c]=0
            chess[r][c]='.'

    return

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



def postprocess(rlt):
    res=[]
    for row in rlt:
        # print "TTT",row
        res.append(''.join(row))
    # print res
    return res






# print solveNQueens(4)



