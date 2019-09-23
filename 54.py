def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if matrix==None:
        return None

    # //consider how to select next step based on current step
    #     #
    #     # so we need init the mtx
    m=len(matrix)
    n=len(matrix[0])
    mtx=[[0 for i in range(n)] for j in range(m)]
    i=0
    j=0
    res=[matrix[i][j]]
    mtx[i][j]=1
    count=1

    while count<m*n:
        while j+1<n and mtx[i][j+1]==0:
            count=count+1
            mtx[i][j+1]=1
            j=j+1
            res.append(matrix[i][j])
        while i+1<n and mtx[i+1][j] == 0:
            count = count + 1
            mtx[i+1][j] = 1
            i=i+1
            res.append(matrix[i][j])
        while j-1>=0 and mtx[i][j - 1] == 0:
            count = count + 1
            mtx[i][j-1] = 1
            j = j - 1
            res.append(matrix[i][j])
        while i-1>=0and mtx[i-1][j]==0:
            count=count+1
            mtx[i - 1][j]=1
            i=i-1
            res.append(matrix[i][j])
    print mtx
    print count

    return res


test1=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print spiralOrder(test1)
print len(test1)
print len(test1[0])