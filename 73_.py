def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    row=len(matrix)
    col=len(matrix[0])
    row1=1

    for i in range(row):
        for j in range(col):
            if matrix[0][j]==0:

            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix

