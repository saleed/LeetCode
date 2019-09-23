def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix==None or len(matrix)==0:
        return False
    row =0
    col=len(matrix[0])-1
    while row<len(matrix) and col>=0:
        if matrix[row][col]==target:
            return True
        while col>=0 and matrix[row][col]>target:
            col=col-1
        while row<len(matrix) and matrix[row][col]<target:
            row=row+1
    return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print searchMatrix(matrix,50)