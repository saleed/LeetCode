class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return
        summtx=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 and j==0:
                    summtx[0][0]=matrix[0][0]
                elif i==0 and j!=0:
                    summtx[i][j]=summtx[0][j-1]+matrix[0][j]
                elif i!=0 and j==0:
                    summtx[i][j]=summtx[i-1][0]+matrix[i][0]
                else:
                    summtx[i][j]=summtx[i-1][j]+summtx[i][j-1]-summtx[i-1][j-1]+matrix[i][j]

        self.summtx=summtx
        self.matrix=matrix
        print self.summtx




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0:
            return self.summtx[row2][col2]
        elif row1==0 and col1!=0:
            return self.summtx[row2][col2]-self.summtx[row2][col1-1]
        elif row1!=0 and col1==0:
            return self.summtx[row2][col2]-self.summtx[row1-1][col2]
        else:
            return self.summtx[row2][col2]-self.summtx[row2][col1-1]-self.summtx[row1-1][col2]+self.summtx[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
a=NumMatrix(matrix)

print a.sumRegion(2,1,4,3)
print a.sumRegion(1,1,2,2)
print a.sumRegion(1,2,2,4)

