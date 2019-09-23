class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        row=0
        col=len(matrix[0])-1
        while row>=0 and row<len(matrix) and col>=0 and col<len(matrix[0]):
            if matrix[row][col]==target:
                return True
            while col>=0 and  matrix[row][col]>target:
                col-=1
            while row<len(matrix) and matrix[row][col]<target:
                row+=1
        return False


